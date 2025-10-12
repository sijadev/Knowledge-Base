---
autor: Simon Janke
title: Anhang - Übersicht aller Ressourcen
type: Index
date: 2025-10-12
tags:
  - index
  - übersicht
  - ressourcen
---

# 📚 Anhang - Komplett-Übersicht

Willkommen im Anhang! Hier findest du alle ergänzenden Ressourcen, Cheat Sheets, Übungen und praktischen Hilfen für deinen Data Analytics Lernweg.

---

## 🗂️ Inhaltsverzeichnis

### 📊 Cheat Sheets
Schnelle Referenzen für tägliche Arbeit

### 🎯 Übungsaufgaben
Praktische Aufgaben mit Lösungen zum Üben

### 📖 Glossar & Referenz
Nachschlagewerke und Begriffserklärungen

### ⚠️ Fehler & Best Practices
Lerne aus häufigen Fehlern

### 💼 Praxis-Szenarien
Real-world Beispiele mit vollständigen Lösungswegen

---

## 📊 Cheat Sheets

### [[SQL-Cheat-Sheet.md]]
**Für:** SQL-Abfragen, Joins, Aggregationen, Window Functions  
**Wann nutzen:** Bei täglicher SQL-Arbeit, BigQuery, Datenbank-Abfragen

**Inhalt:**
- Grundlegende SELECT-Abfragen
- WHERE, GROUP BY, HAVING
- JOINs (INNER, LEFT, RIGHT, FULL)
- Aggregationsfunktionen (SUM, AVG, COUNT)
- Datumsfunktionen (BigQuery-spezifisch)
- Window Functions (ROW_NUMBER, RANK, LAG, LEAD)
- CTEs (Common Table Expressions)
- Subqueries
- Performance-Tipps
- Häufige Analyse-Pattern (RFM, Cohorts)

**Quick Links:**
```sql
-- Schnellzugriff
- Basis-Queries: Seite 1-2
- JOINs: Seite 3-4
- Aggregationen: Seite 2
- Window Functions: Seite 7
- Cohort-Analyse: Seite 9
```

---

### [[Spreadsheets-Cheat-Sheet.md]]
**Für:** Google Sheets, Excel-Formeln  
**Wann nutzen:** Schnelle Analysen, Ad-hoc Berechnungen, Datenexploration

**Inhalt:**
- Mathematische Operatoren
- Aggregationsfunktionen (SUM, AVERAGE, COUNT)
- Lookup-Funktionen (VLOOKUP, XLOOKUP, INDEX/MATCH)
- Text-Funktionen (CONCATENATE, LEFT, RIGHT, MID)
- Datumsfunktionen
- Logische Funktionen (IF, AND, OR, IFERROR)
- Array-Formeln (Google Sheets QUERY, FILTER)
- Pivot-Tabellen
- Häufige Use Cases
- Shortcuts

**Quick Links:**
```
- VLOOKUP: Seite 2
- IF-Formeln: Seite 5
- Datumsberechnungen: Seite 4
- ARRAYFORMULA (Google Sheets): Seite 7
```

---

### [[Data-Visualization-Cheat-Sheet.md]]
**Für:** Tableau, Looker, Chart-Auswahl, Dashboard-Design  
**Wann nutzen:** Beim Erstellen von Visualisierungen und Dashboards

**Inhalt:**
- Chart-Auswahl-Matrix (wann welchen Typ?)
- Vergleichs-Charts (Bar, Column)
- Trend-Charts (Line, Area)
- Teil-vom-Ganzen (Pie, Treemap)
- Verteilungs-Charts (Histogram, Box Plot)
- Beziehungs-Charts (Scatter, Bubble)
- Farbtheorie & Farbpaletten
- Dashboard-Layout-Prinzipien
- KPI-Design
- Häufige Fehler und Fixes
- Tool-spezifische Tipps (Tableau, Looker)

**Quick Links:**
```
- Chart-Auswahl: Seite 1-2
- Farb-Best-Practices: Seite 5
- Dashboard-Design: Seite 7
- Häufige Fehler: Seite 9
```

---

## 🎯 Übungsaufgaben

### [[SQL-Übungen.md]]
**Level:** Anfänger bis Fortgeschritten  
**Geschätzte Zeit:** 4-6 Stunden für alle Aufgaben

**Struktur:**
- **Level 1 (Anfänger):** Basis-Queries, WHERE, einfache Aggregationen
- **Level 2 (Mittelstufe):** JOINs, GROUP BY, Subqueries
- **Level 3 (Fortgeschritten):** CTEs, Window Functions, komplexe Analysen

**Enthält:**
- 5 Aufgaben pro Level
- Musterdatenbank-Schema
- Hinweise für jede Aufgabe
- Vollständige Lösungen mit Erklärungen
- Bonus-Challenge: Customer Retention Report

**Empfohlener Workflow:**
```
1. Lies die Aufgabe
2. Versuche selbst zu lösen (15-30 Min.)
3. Schau Hinweis an wenn stuck
4. Vergleiche mit Musterlösung
5. Verstehe WARUM die Lösung funktioniert
```

---

## 📖 Glossar & Referenz

### [[Glossar-Erweitert.md]]
**Für:** Nachschlagen von Begriffen, Definitionen, Abkürzungen  
**Wann nutzen:** Bei unklaren Begriffen, als Lernhilfe

**Inhalt:**
- **200+ Begriffe** von A-Z
- Klare Definitionen
- Praktische Beispiele
- SQL-spezifische Begriffe
- Häufige Abkürzungen (KPI, ROI, ARPU, etc.)
- Statistische Konzepte
- Business-Metriken

**Besonders nützlich:**
- Korrelation vs. Kausalität
- Window Functions erklärt
- Statistische Begriffe (Median, Standardabweichung, etc.)
- Analytics-Jargon (Churn, Cohort, etc.)

---

## ⚠️ Fehler & Best Practices

### [[Häufige-Fehler.md]]
**Für:** Vermeidung klassischer Fallstricke  
**Wann lesen:** Vor wichtigen Analysen, regelmäßig zur Auffrischung

**Kategorien:**

#### 1. Statistische Fehler
```
✓ Korrelation ≠ Kausalität
✓ P-Hacking vermeiden
✓ Simpson's Paradox
✓ Sample Size beachten
✓ Survivorship Bias
```

#### 2. Datenqualitäts-Fehler
```
✓ Garbage In, Garbage Out
✓ Sampling Bias
✓ Data Leakage
```

#### 3. Analyse-Design-Fehler
```
✓ HARKing vermeiden
✓ One-Size-Fits-All Metrics
✓ Äpfel mit Birnen vergleichen
```

#### 4. Kommunikations-Fehler
```
✓ Fehlender Kontext
✓ Überkomplizierte Visualisierungen
✓ False Precision
```

#### 5. Business-Logic-Fehler
```
✓ Falsche Metrik optimieren
✓ Short-term vs Long-term
✓ Implementation Costs ignorieren
```

**Bonus:**
- Checklisten für Fehler-Prävention
- Quick Reference Card
- Top 10 Fehler zum Ausdrucken

---

### [[Best-Practices.md]]
**Für:** Professionelle Arbeitsweise etablieren  
**Wann nutzen:** Projekt-Start, als Standard-Referenz

**10 Kategorien:**

1. **Projektplanung & Fragestellung**
   - SMART-Fragen
   - Stakeholder-Alignment
   
2. **Datensammlung & -vorbereitung**
   - Datenqualität prüfen
   - Backups erstellen
   
3. **Datenbereinigung**
   - Systematischer Approach
   - Fehlende Daten behandeln
   
4. **Explorative Datenanalyse**
   - Visualisierung für Exploration
   - Hypothesen bilden
   
5. **Datenanalyse & Statistik**
   - Statistisch korrekt denken
   - A/B-Tests richtig durchführen
   
6. **SQL Best Practices**
   - Lesbarkeit
   - Performance-Optimierung
   
7. **Visualisierung & Kommunikation**
   - Chart-Auswahl
   - Storytelling mit Daten
   
8. **Dokumentation**
   - Was dokumentieren?
   - README-Template
   
9. **Reproduzierbarkeit & Versionierung**
   - Git-Workflow
   - Reproduzierbare Analysen
   
10. **Continuous Improvement**
    - Nach jedem Projekt lernen
    - Weiterbildung

**Bonus:**
- Projekt-Review Checkliste
- Templates für verschiedene Dokumente

---

## 💼 Praxis-Szenarien

### [[Praxis-Szenarien.md]]
**Für:** Real-world Anwendung des Gelernten  
**Wann nutzen:** Um zu sehen wie alles zusammenkommt

**4 Vollständige Szenarien:**

#### Szenario 1: E-Commerce Conversion-Drop
```
Problem: 15% Conversion-Drop
Lösung: Schritt-für-Schritt von Frage bis Lösung
Dauer: ~45 Min. zu lesen, zu verstehen und nachzuvollziehen
```
**Was du lernst:**
- Problemspezifizierung
- Hypothesen-getriebene Analyse
- Funnel-Analyse
- Mobile-spezifische Issues
- Action-Plan erstellen

#### Szenario 2: Feature Adoption niedrig
```
Problem: Nur 5% nutzen neues Feature
Lösung: Adoption-Analyse, A/B-Testing, Segmentierung
Dauer: ~30 Min.
```
**Was du lernst:**
- Feature-Metriken definieren
- Hypothesen testen
- Qualitative + Quantitative kombinieren
- Incentive-Testing

#### Szenario 3: Executive Dashboard
```
Problem: CEO braucht Business-Health Dashboard
Lösung: Metrik-Hierarchie, Dashboard-Design
Dauer: ~30 Min.
```
**Was du lernst:**
- Stakeholder-Interview
- Metriken priorisieren
- Dashboard-Layout
- Automatisierung

#### Szenario 4: Pricing Optimization
```
Problem: Sollten wir Preis erhöhen?
Lösung: Elastizitäts-Analyse, Revenue-Simulation
Dauer: ~25 Min.
```
**Was du lernst:**
- Price Sensitivity
- Scenario Analysis
- Revenue Modeling
- Recommendations mit Trade-offs

---

## 🎓 Wie nutze ich den Anhang am besten?

### Für Anfänger
```
Woche 1-2: 
✓ Glossar durchblättern (nicht alles auswendig!)
✓ SQL-Cheat-Sheet anschauen
✓ Spreadsheet-Cheat-Sheet durchgehen

Woche 3-4:
✓ SQL-Übungen Level 1
✓ Best Practices lesen (Projektplanung, Datenqualität)
✓ Häufige Fehler (Statistische Fehler)

Woche 5+:
✓ SQL-Übungen Level 2-3
✓ Praxis-Szenarien durcharbeiten
✓ Visualization-Cheat-Sheet
```

### Für Fortgeschrittene
```
Als Referenz:
✓ Cheat Sheets beim Arbeiten offen haben
✓ Häufige Fehler vor wichtigen Projekten lesen
✓ Best-Practices Checkliste nutzen

Zur Vertiefung:
✓ Praxis-Szenarien eigene Lösungen entwickeln
✓ SQL-Übungen als Workout
✓ Visualisierung-Skills auffrischen
```

### Als Nachschlagewerk
```
Situation → Ressource:

"Wie macht man einen LEFT JOIN nochmal?"
→ SQL-Cheat-Sheet, Seite 3

"Welchen Chart-Typ für Zeitreihe?"
→ Visualization-Cheat-Sheet, Seite 1

"Was bedeutet 'Churn' nochmal?"
→ Glossar, Buchstabe C

"Wie verhindert man P-Hacking?"
→ Häufige Fehler, Kategorie 1

"Wie dokumentiere ich mein Projekt?"
→ Best Practices, Abschnitt 8
```

---

## 📈 Lernpfad-Empfehlungen

### Path 1: SQL-Fokus
```
1. SQL-Cheat-Sheet studieren
2. SQL-Übungen Level 1-3 durcharbeiten
3. Best Practices: SQL-Sektion
4. Praxis-Szenario 1 & 4 (nutzen viel SQL)
```

### Path 2: Visualization-Fokus
```
1. Visualization-Cheat-Sheet
2. Best Practices: Kommunikation & Visualisierung
3. Häufige Fehler: Kommunikation
4. Praxis-Szenario 3 (Dashboard)
```

### Path 3: Analytics-Mindset
```
1. Best Practices komplett lesen
2. Häufige Fehler alle Kategorien
3. Alle 4 Praxis-Szenarien
4. Eigene Mini-Projekte starten
```

---

## 🔄 Wartung & Updates

**Letzte Aktualisierung:** Oktober 2025  
**Version:** 1.0

**Geplante Updates:**
- R Programming Cheat Sheet (Q4 2025)
- Python für Data Analysis (Q1 2026)
- Mehr Praxis-Szenarien (laufend)
- Video-Tutorials Links (Q4 2025)

**Feedback:**
Hast du Verbesserungsvorschläge? Fehlt dir eine Ressource?  
Notiere es in deinen Projektnotizen!

---

## 📎 Quick Access Links

**Jeden Tag nützlich:**
- [[SQL-Cheat-Sheet.md]]
- [[Spreadsheets-Cheat-Sheet.md]]
- [[Glossar-Erweitert.md]]

**Vor wichtigen Projekten:**
- [[Best-Practices.md]]
- [[Häufige-Fehler.md]]

**Zum Üben:**
- [[SQL-Übungen.md]]
- [[Praxis-Szenarien.md]]

**Für Visualisierungen:**
- [[Data-Visualization-Cheat-Sheet.md]]

---

## 🎯 Challenge: 30-Tage Data Analytics

Nutze den Anhang für eine strukturierte 30-Tage Challenge:

**Woche 1: Foundations**
- Tag 1-2: SQL-Cheat-Sheet + Level 1 Übungen
- Tag 3-4: Spreadsheets-Cheat-Sheet + Experimente
- Tag 5-7: Best Practices (Sektion 1-3)

**Woche 2: Deep Dive**
- Tag 8-10: SQL Level 2 Übungen
- Tag 11-12: Häufige Fehler (Kategorie 1-2)
- Tag 13-14: Visualization-Cheat-Sheet

**Woche 3: Advanced**
- Tag 15-17: SQL Level 3 Übungen
- Tag 18-19: Häufige Fehler (Kategorie 3-5)
- Tag 20-21: Best Practices (Sektion 4-7)

**Woche 4: Praxis**
- Tag 22-23: Praxis-Szenario 1
- Tag 24-25: Praxis-Szenario 2
- Tag 26-27: Praxis-Szenario 3
- Tag 28-29: Praxis-Szenario 4
- Tag 30: Review & eigenes Mini-Projekt

---

## 💡 Tipps zur effektiven Nutzung

**1. Drucke wichtige Seiten aus**
```
Empfohlen:
- SQL-Cheat-Sheet erste 3 Seiten
- Top 10 Fehler
- Chart-Auswahl-Matrix
→ Neben deinem Arbeitsplatz aufhängen
```

**2. Erstelle eigene Zusammenfassungen**
```
Nach jedem Dokument:
- 3 wichtigste Learnings notieren
- 1 Sache die du ab morgen anders machst
- 1 Frage die noch offen ist
```

**3. Praxis, Praxis, Praxis**
```
Theorie: 20%
Übungen: 30%
Eigene Projekte: 50%

→ Nutze Cheat Sheets als Referenz während eigener Projekte
```

**4. Teach to Learn**
```
Erkläre Konzepte anderen:
- Kollegen
- Study Group
- Blog Post
- LinkedIn Post

→ Wenn du es nicht erklären kannst, verstehst du es nicht
```

---

## ✅ Anhang-Checkliste

Hake ab was du bereits kennst:

**Cheat Sheets:**
- [ ] SQL-Cheat-Sheet gelesen
- [ ] Spreadsheets-Cheat-Sheet gelesen
- [ ] Visualization-Cheat-Sheet gelesen

**Übungen:**
- [ ] SQL Level 1 abgeschlossen
- [ ] SQL Level 2 abgeschlossen
- [ ] SQL Level 3 abgeschlossen
- [ ] Bonus-Challenge versucht

**Referenz:**
- [ ] Glossar durchgeblättert
- [ ] Wichtige Begriffe markiert

**Best Practices & Fehler:**
- [ ] Best Practices gelesen
- [ ] Häufige Fehler gelesen
- [ ] Checklisten genutzt

**Praxis:**
- [ ] Szenario 1 durchgearbeitet
- [ ] Szenario 2 durchgearbeitet
- [ ] Szenario 3 durchgearbeitet
- [ ] Szenario 4 durchgearbeitet

---

**🎉 Herzlichen Glückwunsch zu dieser umfangreichen Ressourcen-Sammlung!**

Diese Materialien werden dich durch deine gesamte Data Analytics Journey begleiten - vom Anfänger bis zum erfahrenen Analyst.

**Remember:** 
- Perfektion ist der Feind von Fortschritt
- Jeder Fehler ist eine Lerngelegenheit
- Kontinuierliche Praxis ist der Schlüssel

**Viel Erfolg! 🚀**

---

*Erstellt: Oktober 2025*  
*Für: Google Data Analytics Zertifizierung & Beyond*