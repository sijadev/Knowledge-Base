-- Kategorien für Ticketklassifizierung
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Fachbereiche/Departements
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tickettypen
CREATE TABLE ticket_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
    -- z.B.: Incident, Request, Problem, Change
);

-- Keywords/Tags für flexible Suche
CREATE TABLE keywords (
    id SERIAL PRIMARY KEY,
    keyword VARCHAR(100) NOT NULL UNIQUE,
    usage_count INTEGER DEFAULT 0
    -- usage_count zeigt, wie oft ein Keyword benutzt wird
);

-- ============================================================================
-- 2. HAUPTTABELLE: SOLUTIONS (Tickets/Lösungen)
-- ============================================================================

CREATE TABLE solutions (
    id SERIAL PRIMARY KEY,
    ticket_number VARCHAR(20) NOT NULL UNIQUE,
    -- Eindeutige Ticketnummer (z.B. TK-2025-00001)

    category_id INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    ticket_type_id INTEGER NOT NULL,
    -- Fremdschlüssel zu Referenztabellen

    priority VARCHAR(20) DEFAULT 'Medium',
    -- Low, Medium, High, Critical

    status VARCHAR(20) DEFAULT 'Offen',
    -- Offen, In Bearbeitung, Gelöst, Geschlossen

    kurzbeschreibung VARCHAR(255) NOT NULL,
    -- Zusammenfassung des Problems

    detaillierte_beschreibung TEXT,
    -- Vollständige Problembeschreibung

    loesung_text TEXT,
    -- Die Lösungsbeschreibung

    ursache TEXT,
    -- Wurzelursache (für zukünftige Optimierung)

    eingangsdatum TIMESTAMP NOT NULL,
    -- Wann das Ticket eingegangen ist

    loesungsdatum TIMESTAMP,
    -- Wann die Lösung umgesetzt wurde

    abschlussdatum TIMESTAMP,
    -- Wann das Ticket geschlossen wurde

    bearbeiter VARCHAR(100),
    -- Name des zuständigen Supporters

    zeitaufwand_minuten INTEGER DEFAULT 0,
    -- Gesamte Bearbeitungszeit

    loesung_qualitaet INTEGER DEFAULT 0,
    -- Bewertung 1-5 (später für Relevanzsortierung)

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Fremdschlüssel definieren
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES categories(id),
    CONSTRAINT fk_department FOREIGN KEY (department_id) REFERENCES departments(id),
    CONSTRAINT fk_ticket_type FOREIGN KEY (ticket_type_id) REFERENCES ticket_types(id)
);

-- Indizes für bessere Performance
CREATE INDEX idx_eingangsdatum ON solutions(eingangsdatum DESC);
CREATE INDEX idx_category_department ON solutions(category_id, department_id);
CREATE INDEX idx_status ON solutions(status);
CREATE INDEX idx_ticket_number ON solutions(ticket_number);
CREATE INDEX idx_bearbeiter ON solutions(bearbeiter);
CREATE INDEX idx_status_eingangsdatum ON solutions(status, eingangsdatum DESC);
CREATE INDEX idx_priority_status ON solutions(priority, status);

-- Volltextsuche Index (Tsvector)
ALTER TABLE solutions ADD COLUMN search_vector tsvector;
CREATE INDEX idx_search_vector ON solutions USING GIN(search_vector);

-- ============================================================================
-- 3. VERKNÜPFUNGSTABELLE: Keywords (Many-to-Many)
-- ============================================================================

CREATE TABLE solution_keywords (
    solution_id INTEGER NOT NULL,
    keyword_id INTEGER NOT NULL,
    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (solution_id, keyword_id),
    CONSTRAINT fk_solution FOREIGN KEY (solution_id) REFERENCES solutions(id) ON DELETE CASCADE,
    CONSTRAINT fk_keyword FOREIGN KEY (keyword_id) REFERENCES keywords(id) ON DELETE CASCADE
);

CREATE INDEX idx_keyword ON solution_keywords(keyword_id);

-- ============================================================================
-- 4. ARBEITSLOG (Work Log / Activity Log)
-- ============================================================================

CREATE TABLE worklog (
    id SERIAL PRIMARY KEY,
    solution_id INTEGER NOT NULL,

    log_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    aktion VARCHAR(50),
    -- z.B.: Erstellt, Aktualisiert, Gelöst, Kommentar

    kommentar TEXT,
    -- Detaillierte Beschreibung der Aktion

    technician VARCHAR(100) NOT NULL,
    -- Wer hat die Aktion durchgeführt

    zeit_minuten INTEGER DEFAULT 0,
    -- Zeitaufwand für diese Aktion

    old_status VARCHAR(20),
    -- Status vor der Änderung (für Änderungsverfolgung)

    new_status VARCHAR(20),
    -- Status nach der Änderung

    CONSTRAINT fk_solution_worklog FOREIGN KEY (solution_id) REFERENCES solutions(id) ON DELETE CASCADE
);

CREATE INDEX idx_solution_date ON worklog(solution_id, log_date);
CREATE INDEX idx_technician ON worklog(technician);

-- ============================================================================
-- 4. ARBEITSLOG (Work Log / Activity Log)
-- ============================================================================

CREATE TABLE worklog (
    id SERIAL PRIMARY KEY,
    solution_id INTEGER NOT NULL,

    log_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    aktion VARCHAR(50),
    -- z.B.: Erstellt, Aktualisiert, Gelöst, Kommentar

    kommentar TEXT,
    -- Detaillierte Beschreibung der Aktion

    technician VARCHAR(100) NOT NULL,
    -- Wer hat die Aktion durchgeführt

    zeit_minuten INTEGER DEFAULT 0,
    -- Zeitaufwand für diese Aktion

    old_status VARCHAR(20),
    -- Status vor der Änderung (für Änderungsverfolgung)

    new_status VARCHAR(20),
    -- Status nach der Änderung

    CONSTRAINT fk_solution_worklog FOREIGN KEY (solution_id) REFERENCES solutions(id) ON DELETE CASCADE
);

CREATE INDEX idx_solution_date ON worklog(solution_id, log_date);
CREATE INDEX idx_technician ON worklog(technician);

-- ============================================================================
-- 5. TRIGGER FÜR AUTOMATISCHE AKTUALISIERUNG
-- ============================================================================

-- Trigger für updated_at aktualisieren
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_solutions_modified BEFORE UPDATE ON solutions
    FOR EACH ROW EXECUTE FUNCTION update_modified_column();

-- Trigger für Volltextsuche aktualisieren
CREATE OR REPLACE FUNCTION update_search_vector()
RETURNS TRIGGER AS $$
BEGIN
    NEW.search_vector := to_tsvector('german',
        COALESCE(NEW.kurzbeschreibung, '') || ' ' ||
        COALESCE(NEW.detaillierte_beschreibung, '')
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_solutions_search_vector BEFORE INSERT OR UPDATE ON solutions
    FOR EACH ROW EXECUTE FUNCTION update_search_vector();

-- Trigger für Usage Count von Keywords aktualisieren
CREATE OR REPLACE FUNCTION update_keyword_usage_count()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE keywords SET usage_count = usage_count + 1 WHERE id = NEW.keyword_id;
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE keywords SET usage_count = usage_count - 1 WHERE id = OLD.keyword_id;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_keyword_usage AFTER INSERT OR DELETE ON solution_keywords
    FOR EACH ROW EXECUTE FUNCTION update_keyword_usage_count();
