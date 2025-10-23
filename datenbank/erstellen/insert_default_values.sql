-- ============================================================================
-- INITIALDATEN EINFÜGEN (Beispiele)
-- ============================================================================

-- Kategorien einfügen
INSERT INTO categories (name, description) VALUES
('Hardware', 'Hardwarefehler und -probleme'),
('Software', 'Softwarefehler und -installationen'),
('Netzwerk', 'Netzwerk- und Konnektivitätsprobleme'),
('Database', 'Datenbankfehler und Performance'),
('System', 'Systemkonfiguration und -probleme');

-- Departements einfügen
INSERT INTO departments (name, description) VALUES
('IT-Infrastruktur', 'Server, Storage, Netzwerk'),
('Anwendungen', 'Business-Software und Tools'),
('Desktop-Support', 'Client-Rechner und Peripherie'),
('Database-Team', 'Datenbankadministration');

-- Tickettypen einfügen
INSERT INTO ticket_types (name, description) VALUES
('Incident', 'Unerwarteter Fehler, der sofortige Hilfe benötigt'),
('Request', 'Anfrage für neue Ressourcen oder Konfiguration'),
('Problem', 'Systemic Issue, die wiederkehrend ist'),
('Change', 'Geplante Änderung oder Update');

-- Keywords einfügen
INSERT INTO keywords (keyword) VALUES
('DNS'),
('Server nicht erreichbar'),
('Passwort'),
('VPN'),
('Email'),
('Login fehlgeschlagen'),
('Performance'),
('Crash'),
('Disk Space'),
('Update');
