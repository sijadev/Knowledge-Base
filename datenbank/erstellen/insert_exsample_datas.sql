-- Beispielticket einfügen
INSERT INTO solutions
(ticket_number, category_id, department_id, ticket_type_id, priority, status,
 kurzbeschreibung, detaillierte_beschreibung, loesung_text, eingangsdatum, bearbeiter, zeitaufwand_minuten, loesung_qualitaet)
VALUES
(
    'TK-2025-00001',
    3,
    1,
    1,
    'High',
    'Gelöst',
    'Benutzer kann sich nicht in VPN einloggen',
    'Mehrere Benutzer berichten von VPN-Verbindungsproblemen. Fehler beim Verbindungsaufbau mit Timeout.',
    'VPN-Certificate war abgelaufen. Neues Zertifikat generiert und auf VPN-Server aktualisiert. Benutzer aufgefordert, VPN-Client neu zu starten.',
    '2025-10-15 08:30:00',
    'Max Mustermann',
    45,
    5
);

-- Keywords zum Ticket hinzufügen
INSERT INTO solution_keywords (solution_id, keyword_id) VALUES
(1, 4), -- VPN
(1, 6); -- Login fehlgeschlagen

-- Arbeitslog-Einträge hinzufügen
INSERT INTO worklog (solution_id, aktion, kommentar, technician, zeit_minuten, old_status, new_status) VALUES
(1, 'Erstellt', 'Ticket vom Benutzer gemeldet', 'Support-Queue', 0, NULL, 'Offen'),
(1, 'Aktualisiert', 'Analyse durchgeführt, Root-Cause identifiziert', 'Max Mustermann', 20, 'Offen', 'In Bearbeitung'),
(1, 'Gelöst', 'VPN-Certificate erneuert, Benutzer bestätigt Funktionsfähigkeit', 'Max Mustermann', 25, 'In Bearbeitung', 'Gelöst');