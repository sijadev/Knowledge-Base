-- ============================================================================
-- SEARCH-QUERIES
-- ============================================================================

-- QUERY 1: Volltextsuche (mit Ranking)
-- Sucht in Kurzbeschreibung und Detailbeschreibung
SELECT
    s.id,
    s.ticket_number,
    s.kurzbeschreibung,
    s.eingangsdatum,
    s.status,
    c.name AS kategorie,
    d.name AS department,
    ts_rank(s.search_vector, query) AS rank
FROM solutions s
JOIN categories c ON s.category_id = c.id
JOIN departments d ON s.department_id = d.id,
plainto_tsquery('german', 'VPN Fehler') query
WHERE s.search_vector @@ query
ORDER BY rank DESC, s.eingangsdatum DESC;

-- QUERY 2: Nach Keyword suchen
-- Findet alle Tickets mit bestimmten Tags
SELECT DISTINCT
    s.id,
    s.ticket_number,
    s.kurzbeschreibung,
    s.eingangsdatum,
    s.status,
    k.keyword
FROM solutions s
JOIN solution_keywords sk ON s.id = sk.solution_id
JOIN keywords k ON sk.keyword_id = k.id
WHERE k.keyword = 'VPN'
ORDER BY s.eingangsdatum DESC;

-- QUERY 3: Kombinierte erweiterte Suche
-- Nach Keyword, Kategorie, Datum und Status
SELECT
    s.id,
    s.ticket_number,
    s.kurzbeschreibung,
    s.eingangsdatum,
    s.status,
    s.bearbeiter,
    c.name AS kategorie,
    d.name AS department,
    STRING_AGG(k.keyword, ', ' ORDER BY k.keyword) AS keywords
FROM solutions s
JOIN categories c ON s.category_id = c.id
JOIN departments d ON s.department_id = d.id
LEFT JOIN solution_keywords sk ON s.id = sk.solution_id
LEFT JOIN keywords k ON sk.keyword_id = k.id
WHERE c.id = 3
  AND d.id = 1
  AND s.eingangsdatum >= CURRENT_TIMESTAMP - INTERVAL '3 months'
  AND s.status IN ('Gelöst', 'Geschlossen')
GROUP BY s.id, s.ticket_number, s.kurzbeschreibung, s.eingangsdatum, s.status,
         s.bearbeiter, c.name, d.name
ORDER BY s.eingangsdatum DESC
LIMIT 50;

-- QUERY 4: Arbeitslog für ein Ticket anzeigen
SELECT
    w.log_date,
    w.aktion,
    w.kommentar,
    w.technician,
    w.zeit_minuten,
    w.old_status,
    w.new_status
FROM worklog w
WHERE w.solution_id = 1
ORDER BY w.log_date ASC;

-- QUERY 5: Statistik - häufigste Probleme (pro Monat)
SELECT
    TO_CHAR(s.eingangsdatum, 'YYYY-MM') AS monat,
    c.name AS kategorie,
    COUNT(s.id) AS anzahl_tickets,
    ROUND(AVG(s.zeitaufwand_minuten)::numeric, 2) AS durchschnittliche_bearbeitungszeit,
    ROUND(AVG(s.loesung_qualitaet)::numeric, 2) AS durchschnittliche_qualitaet
FROM solutions s
JOIN categories c ON s.category_id = c.id
WHERE s.eingangsdatum >= CURRENT_TIMESTAMP - INTERVAL '30 days'
GROUP BY TO_CHAR(s.eingangsdatum, 'YYYY-MM'), c.id, c.name
ORDER BY monat DESC, anzahl_tickets DESC;

-- QUERY 6: Nach Bearbeiter und Zeitraum filtern
SELECT
    s.ticket_number,
    s.kurzbeschreibung,
    s.eingangsdatum,
    s.loesungsdatum,
    s.status,
    s.zeitaufwand_minuten,
    EXTRACT(EPOCH FROM (s.loesungsdatum - s.eingangsdatum)) / 3600 AS reaktionszeit_stunden,
    c.name AS kategorie
FROM solutions s
JOIN categories c ON s.category_id = c.id
WHERE s.bearbeiter = 'Max Mustermann'
  AND EXTRACT(YEAR FROM s.eingangsdatum) = 2025
  AND EXTRACT(MONTH FROM s.eingangsdatum) = 10
ORDER BY s.eingangsdatum DESC;

-- QUERY 7: Ähnliche bereits gelöste Tickets finden
-- Nützlich bei neuen Tickets: Schau, was ähnliche Probleme waren
SELECT
    s.id,
    s.ticket_number,
    s.kurzbeschreibung,
    s.loesung_text,
    s.loesung_qualitaet,
    COUNT(sk.keyword_id) AS gemeinsame_keywords
FROM solutions s
LEFT JOIN solution_keywords sk ON s.id = sk.solution_id
WHERE s.status IN ('Gelöst', 'Geschlossen')
  AND s.loesung_qualitaet >= 4
  AND sk.keyword_id IN (
    -- Keywords des aktuellen Tickets (z.B. Ticket ID 1)
    SELECT keyword_id FROM solution_keywords WHERE solution_id = 1
  )
GROUP BY s.id, s.ticket_number, s.kurzbeschreibung, s.loesung_text, s.loesung_qualitaet
ORDER BY gemeinsame_keywords DESC, s.loesung_qualitaet DESC
LIMIT 5;

-- QUERY 8: Top Keywords nach Verwendung
SELECT
    k.keyword,
    k.usage_count,
    COUNT(s.id) AS anzahl_tickets
FROM keywords k
LEFT JOIN solution_keywords sk ON k.id = sk.keyword_id
LEFT JOIN solutions s ON sk.solution_id = s.id
GROUP BY k.id, k.keyword, k.usage_count
ORDER BY k.usage_count DESC
LIMIT 20;

-- QUERY 9: Offene Tickets pro Support-Techniker
SELECT
    s.bearbeiter,
    COUNT(s.id) AS offene_tickets,
    COUNT(CASE WHEN s.priority = 'Critical' THEN 1 END) AS kritische_tickets,
    ROUND(AVG(s.zeitaufwand_minuten)::numeric, 2) AS durchschnittliche_bearbeitungszeit
FROM solutions s
WHERE s.status IN ('Offen', 'In Bearbeitung')
GROUP BY s.bearbeiter
ORDER BY kritische_tickets DESC, offene_tickets DESC;

-- QUERY 10: Performance Report - Durchschnittliche Reaktionszeit pro Kategorie
SELECT
    c.name AS kategorie,
    COUNT(s.id) AS tickets_im_monat,
    ROUND(AVG(EXTRACT(EPOCH FROM (s.loesungsdatum - s.eingangsdatum)) / 3600)::numeric, 2) AS reaktionszeit_stunden,
    ROUND(AVG(EXTRACT(EPOCH FROM (s.abschlussdatum - s.eingangsdatum)) / 86400)::numeric, 2) AS geschlossenzeit_tage,
    ROUND(AVG(s.loesung_qualitaet)::numeric, 2) AS durchschnittliche_qualitaet
FROM solutions s
JOIN categories c ON s.category_id = c.id
WHERE s.eingangsdatum >= CURRENT_TIMESTAMP - INTERVAL '30 days'
  AND s.status = 'Geschlossen'
GROUP BY c.id, c.name
ORDER BY reaktionszeit_stunden DESC;