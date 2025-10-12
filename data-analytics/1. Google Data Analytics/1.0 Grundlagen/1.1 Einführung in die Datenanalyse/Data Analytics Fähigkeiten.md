---
autor: Simon Janke
title: Data Analytics Fähigkeiten
type: Google Data Analytics Kurs
date: 2025-10-02
tags:
  - fähigkeiten
  - Grundlagen
  - soft-skills
  - technical-skills
links:
  - "[[Grundlagen]]"
  - "[[Analytisches Denken]]"
---

# 💎 Data Analytics Fähigkeiten - Die 5 Säulen

---

## 1. 🔍 Neugierde

### Definition
Die Fähigkeit und der Drang, die richtigen Fragen zu stellen und tiefer zu graben, um entscheidende Erkenntnisse zu finden.

### Warum wichtig?
- Entdeckt verborgene Muster
- Hinterfragt Annahmen
- Führt zu tieferen Insights
- Treibt Innovation

### Praktische Anwendung

#### Die "5 Warum"-Methode
```
Problem: Website-Conversion ist gesunken

Warum? → Weniger Leute klicken auf "Kaufen"
Warum? → Der Button ist weniger sichtbar
Warum? → Neues Design hat ihn nach unten verschoben
Warum? → Design-Team folgte Mobile-First Approach
Warum? → Keine A/B-Tests vor Launch durchgeführt

→ Root Cause: Fehlender Testing-Prozess
```

#### Neugierig sein in der Praxis
```
❌ Oberflächlich: "Umsatz ist um 10% gestiegen"
✅ Neugierig: 
   - In welchen Regionen genau?
   - Bei welchen Produktkategorien?
   - Zu welchen Tageszeiten?
   - Welche Kundengruppen?
   - Was war der Auslöser?
   - Ist es nachhaltig?
```

#### Fragen, die Neugierde zeigen
```
1. "Was würde passieren wenn...?"
2. "Warum ist das so?"
3. "Gibt es einen Zusammenhang zwischen X und Y?"
4. "Was fehlt uns noch zum vollständigen Bild?"
5. "Welche Annahmen haben wir, die wir testen sollten?"
6. "Was überrascht mich an diesen Daten?"
```

### Neugierde entwickeln

**Übungen:**
1. **Daily Data Dive:** Jeden Tag 15 Min. ein Dashboard explorieren
2. **Question Journal:** Fragen aufschreiben, die während der Arbeit entstehen
3. **Cross-Functional Learning:** Mit anderen Teams sprechen, neue Perspektiven
4. **"Was wäre wenn"-Szenarien:** Hypothesen bilden und testen

### Unterstützt durch kritisches Denken

Neugierde allein reicht nicht - kritisches Denken hilft zu bewerten:
- Sind die Daten vertrauenswürdig?
- Welche Bias könnte existieren?
- Gibt es alternative Erklärungen?
- Was fehlt in der Analyse?

---

## 2. 🎯 Verständnis für den Kontext

### Definition
Die Fähigkeit zu verstehen, **WARUM** Daten das zeigen, was sie zeigen - unter Berücksichtigung des Geschäftskontexts, der Branche und externer Faktoren.

### Warum wichtig?
Ohne Kontext sind Daten nur Zahlen. Mit Kontext werden sie zu Insights.

### Faktoren, die Daten beeinflussen

#### Interne Faktoren
```
✓ Geschäftsstrategie-Änderungen
✓ Marketingkampagnen
✓ Produktlaunches
✓ Preisanpassungen
✓ Technische Änderungen (Website-Updates)
✓ Organisatorische Veränderungen
✓ Kundensupport-Qualität
```

#### Externe Faktoren
```
✓ Saisonalität (Weihnachten, Sommer)
✓ Wirtschaftslage
✓ Wettbewerb
✓ Regulatorische Änderungen
✓ Technologische Trends
✓ Gesellschaftliche Ereignisse
✓ Wetter (z.B. bei Retail)
```

### Praktisches Beispiel

**Situation:** E-Commerce Sales sind im Dezember um 200% gestiegen

**Analyse ohne Kontext:**
```
❌ "Wow, super Performance! Was haben wir richtig gemacht?"
```

**Analyse mit Kontext:**
```
✅ Faktoren berücksichtigen:
   - Dezember = Weihnachtssaison (erwartet!)
   - Black Friday / Cyber Monday
   - Letztes Jahr auch +180%
   - Wettbewerber zeigen ähnlichen Trend
   
→ Realistische Einschätzung: Performance ist gut, aber nicht außergewöhnlich
→ Frage: Warum nur 200% und nicht 250% wie Wettbewerb?
```

### Kontext-Checkliste

Vor jeder Analyse fragen:
```
1. Zeitlicher Kontext
   □ Gibt es saisonale Muster?
   □ Wann war das letzte große Event?
   □ Vergleichszeitraum angemessen?

2. Geschäftlicher Kontext
   □ Welche Initiativen liefen parallel?
   □ Gab es Produktänderungen?
   □ Welche Business-Ziele sind relevant?

3. Technischer Kontext
   □ Tracking-Änderungen?
   □ Datendefinitionen gleich geblieben?
   □ Bekannte Datenqualitätsprobleme?

4. Externer Kontext
   □ Branchentrends?
   □ Makroökonomische Entwicklung?
   □ Wettbewerber-Aktivitäten?
```

### Kontext-Verständnis entwickeln

**Praktische Tipps:**
1. **Stakeholder-Gespräche:** Regelmäßig mit Business-Teams sprechen
2. **Industrie-News:** Branchentrends verfolgen
3. **Historical Context:** Vergangene Analysen und Reports lesen
4. **Cross-Functional Meetings:** An verschiedenen Team-Meetings teilnehmen

---

## 3. 🛠️ Technische Herangehensweise

### Definition
Die Fähigkeit, komplexe Probleme in handhabbare, strukturierte Teile zu zerlegen und systematisch zu lösen.

### Von Grob zu Fein - Die Pyramide

```
Level 1: Geschäftsproblem (Sehr Grob)
"Umsatz ist gesunken"
         ↓
Level 2: Bereiche identifizieren (Grob)
- Region A, B, C?
- Produkt X, Y, Z?
- Online vs. Offline?
         ↓
Level 3: Spezifische Segmente (Mittel)
- Online + Produkt X + Region A
         ↓
Level 4: Granulare Analyse (Fein)
- Welche Kundensegmente in Region A?
- Welche Wochentage?
- Welche Kanäle?
         ↓
Level 5: Root Cause (Sehr Fein)
- Spezifische Ursache identifiziert
```

### Praktisches Beispiel: Debugging-Ansatz

**Problem:** Dashboard zeigt falsche Zahlen

**Technische Herangehensweise:**
```
Schritt 1: Problem eingrenzen
- Welche Metriken sind falsch?
- Seit wann?
- Für alle User oder nur bestimmte?

Schritt 2: Komponenten identifizieren
Dashboard = Datenquelle + Transformation + Visualisierung

Schritt 3: Einzeln testen
✓ Datenquelle korrekt? → SQL direkt prüfen
✓ Transformation korrekt? → Zwischenschritte validieren
✓ Visualisierung korrekt? → Rohdaten vs. dargestellt

Schritt 4: Problem isolieren
→ Transformation-Layer hat Fehler

Schritt 5: Fehler eingrenzen
→ JOIN erzeugt Duplikate

Schritt 6: Fix implementieren
→ DISTINCT oder GROUP BY hinzufügen

Schritt 7: Validieren
→ Stichproben prüfen, Edge Cases testen
```

### Problemlösungs-Framework

#### 1. Define (Definiere)
```
- Was genau ist das Problem?
- Was ist das erwartete Ergebnis?
- Was sind die Constraints?
```

#### 2. Decompose (Zerlege)
```
- In welche Teilprobleme kann ich zerlegen?
- Welche Komponenten sind beteiligt?
- Gibt es Dependencies?
```

#### 3. Prioritize (Priorisiere)
```
- Welcher Teil hat größten Impact?
- Was ist am einfachsten zu lösen?
- Quick Wins vs. Long-term Solutions?
```

#### 4. Execute (Führe aus)
```
- Schritt für Schritt lösen
- Zwischenergebnisse validieren
- Dokumentieren während des Prozesses
```

#### 5. Validate (Validiere)
```
- Funktioniert die Lösung?
- Edge Cases getestet?
- Langfristig stabil?
```

### Tools für technische Herangehensweise

**Flowcharts:** Prozesse visualisieren
**Pseudocode:** Logik vor Implementierung planen
**Checklisten:** Systematisch abarbeiten
**Testing-Frameworks:** Automatisiert validieren

---

## 4. 🎨 Datendesign

### Definition
Die Kunst, Informationen so zu **organisieren und strukturieren**, dass Muster erkennbar werden und Insights leicht zu finden sind.

### Dimensionen des Datendesigns

#### 1. Datenstruktur-Design
```
Entscheidungen:
- Welche Tabellen/Sheets?
- Welche Spalten?
- Welche Datentypen?
- Normalisiert vs. Denormalisiert?
- Hierarchien und Beziehungen?
```

**Beispiel: E-Commerce Schema**
```
Gut strukturiert:
├── customers (customer_id, name, email, signup_date)
├── products (product_id, name, category, price)
├── orders (order_id, customer_id, order_date, status)
└── order_items (order_item_id, order_id, product_id, quantity)

Jede Tabelle hat klaren Zweck, Redundanz minimiert
```

#### 2. Analyse-Design
```
Wie organisiere ich Daten für Analyse?
- Welche Aggregationslevel?
- Welche Zeitgranularität?
- Welche Dimensionen für Segmentierung?
- Welche Metriken sind abgeleitet?
```

**Beispiel: Sales Analysis Table**
```
sales_summary
├── date (Tag, Monat, Quartal, Jahr)
├── region (Land, Stadt)
├── product (Kategorie, Subkategorie, SKU)
├── customer_segment (VIP, Regular, New)
├── sales_amount
├── quantity
├── profit
└── customer_count

→ Multi-dimensionale Analyse möglich
```

#### 3. Visualisierungs-Design
```
- Welche Charttypen für welche Insights?
- Wie viele Charts pro Dashboard?
- Welche Drill-Down-Hierarchie?
- Farben für Kategorien vs. Heatmaps?
```

### Prinzipien guten Datendesigns

#### KISS - Keep It Simple, Stupid
```
✅ Einfache, klare Strukturen
✅ Selbsterklärende Spaltennamen
✅ Konsistente Namenskonventionen
✅ Minimale aber ausreichende Felder

❌ Über-komplizierte Strukturen
❌ Kryptische Abkürzungen
❌ Inkonsistente Formate
```

#### DRY - Don't Repeat Yourself
```
✅ Jede Information nur einmal speichern
✅ Berechnungen in Views/Formeln, nicht als Spalten
✅ Referenztabellen statt Duplikate

❌ Gleiche Daten in mehreren Tabellen
❌ Berechnete Werte als redundante Spalten
```

#### Separation of Concerns
```
Rohdaten ≠ Transformierte Daten ≠ Präsentations-Layer

Layer 1: Raw Data (unverändert)
Layer 2: Cleaned Data (bereinigt)
Layer 3: Analytics Tables (aggregiert)
Layer 4: Visualizations (präsentiert)
```

### Praktisches Beispiel: Dashboard-Design

**Schlecht designed:**
```
❌ 15 verschiedene Charts auf einer Seite
❌ Keine klare visuelle Hierarchie
❌ Jeder Chart in anderen Farben
❌ Keine Storyline
```

**Gut designed:**
```
✅ Pyramidale Struktur:
   Top: 3-4 Key Metrics (größte Charts)
   Middle: 4-6 Supporting Metrics
   Bottom: Detaillierte Breakdowns
   
✅ Konsistentes Farbschema:
   - Blau für Hauptmetriken
   - Grün für positive Trends
   - Rot für Probleme/Alerts
   
✅ Logischer Flow:
   Left-to-Right, Top-to-Bottom
   Erzählt eine Geschichte
```

---

## 5. 📊 Datenstrategie

### Definition
Das Management der **Menschen, Prozesse und Tools**, die bei der Datenanalyse eingesetzt werden.

### Die drei Säulen

#### 1. Menschen (People)
```
Wer ist involviert?
- Data Analysts
- Data Engineers
- Business Stakeholders
- IT/DevOps

Rollen & Verantwortlichkeiten:
- Wer sammelt Daten?
- Wer validiert Qualität?
- Wer erstellt Reports?
- Wer trifft Entscheidungen?

Skills Development:
- Training für neue Tools
- Best Practices teilen
- Mentoring-Programme
```

#### 2. Prozesse (Processes)
```
Wie arbeiten wir mit Daten?

Data Collection:
- Automatisiert vs. Manuell
- Frequenz (täglich, wöchentlich?)
- Qualitätschecks

Data Analysis:
- Standard-Workflows
- Review-Prozesse
- Dokumentations-Standards

Decision Making:
- Wer muss eingebunden werden?
- Wie werden Insights kommuniziert?
- Follow-up-Prozesse
```

#### 3. Tools (Technology)
```
Welche Tools nutzen wir?

Data Storage:
- Data Warehouse (BigQuery, Snowflake)
- Databases (PostgreSQL, MySQL)

Analysis Tools:
- SQL Clients
- Python/R
- Spreadsheets

Visualization:
- Tableau
- Looker
- Power BI

Collaboration:
- Documentation (Notion, Confluence)
- Version Control (Git)
- Communication (Slack, Teams)
```

### Datenstrategie entwickeln

#### Phase 1: Assessment
```
Status Quo verstehen:
□ Welche Datenquellen haben wir?
□ Welche Tools nutzen wir bereits?
□ Welche Skills hat das Team?
□ Wo sind die Schmerzpunkte?
□ Was sind unsere Ziele?
```

#### Phase 2: Planning
```
Roadmap erstellen:
1. Quick Wins (0-3 Monate)
   - Low-hanging fruit
   - Sichtbare Erfolge
   
2. Foundation (3-6 Monate)
   - Infrastruktur aufbauen
   - Standards etablieren
   
3. Scale (6-12 Monate)
   - Automatisierung
   - Advanced Analytics
```

#### Phase 3: Execution
```
Iterativ umsetzen:
→ Start small, prove value
→ Learn and adjust
→ Scale what works
→ Deprecate what doesn't
```

#### Phase 4: Governance
```
Langfristig sichern:
- Data Quality Monitoring
- Access Management
- Compliance (GDPR, etc.)
- Documentation uptodate halten
```

### Praktisches Beispiel: Daten-Strategie für Startup

**Situation:** Startup mit 50 Mitarbeitern, wachsend

**Strategie:**

**Phase 1 (Monat 1-3):**
```
People:
- 1 Data Analyst einstellen
- Stakeholder-Interviews durchführen

Processes:
- Weekly Data Review Meeting
- Standard-SQL-Queries dokumentieren

Tools:
- BigQuery als Data Warehouse
- Google Sheets für Ad-hoc
- Looker Studio für Dashboards
```

**Phase 2 (Monat 3-6):**
```
People:
- Data Engineering Support
- Training für Stakeholder

Processes:
- ETL Pipelines automatisieren
- Data Quality Checks

Tools:
- dbt für Transformationen
- Airflow für Orchestration
```

**Phase 3 (Monat 6-12):**
```
People:
- Data Team auf 3 Personen wachsen
- Analytics Champions in jedem Team

Processes:
- Self-Service Analytics enablen
- Advanced Analytics Projekte

Tools:
- Python/R für ML
- A/B Testing Platform
```

---

## 🎯 Die 5 Fähigkeiten in Kombination

Ein exzellenter Data Analyst nutzt ALLE 5 Fähigkeiten zusammen:

### Beispiel-Projekt: Kundenabwanderung reduzieren

**1. Neugierde:**
```
"Warum verlassen Kunden uns? 
Gibt es Muster? 
Was unterscheidet loyale von abgewanderten Kunden?"
```

**2. Kontext:**
```
"Preiserhöhung vor 3 Monaten
Konkurrent hat neues Feature gelauncht
Wirtschaftliche Unsicherheit
→ Faktoren berücksichtigen"
```

**3. Technische Herangehensweise:**
```
Problem zerlegen:
1. Churn-Rate berechnen
2. Nach Segmenten analysieren
3. Zeitliche Muster identifizieren
4. Prädiktoren finden
5. Intervention testen
```

**4. Datendesign:**
```
Struktur für Analyse schaffen:
- Customer-Level Dataset
- Features: RFM, Support-Tickets, Engagement
- Labels: Churned vs. Active
- Zeitfenster konsistent
```

**5. Datenstrategie:**
```
Stakeholder einbinden:
- Product Team für Features
- Marketing für Retention-Kampagnen
- CS Team für Frühwarnung

Tools definieren:
- SQL für Datenaggregation
- Python für Predictive Modeling
- Tableau für Monitoring-Dashboard

Prozess etablieren:
- Monatliches Churn-Review
- Wöchentliche At-Risk-Liste
- Quarterly Model Re-training
```

---

## 📚 Weiterentwicklung der Fähigkeiten

### Ressourcen

**Für Neugierde:**
- Kaggle Competitions explorieren
- Andere Data-Blogs lesen
- "What would happen if" spielen

**Für Kontext:**
- Branchennews verfolgen
- Mit Stakeholdern sprechen
- Competitor Analysis

**Für Technische Herangehensweise:**
- LeetCode/HackerRank
- System Design lernen
- Debugging üben

**Für Datendesign:**
- Database Design-Kurse
- Visualization-Portfolios ansehen
- UI/UX Prinzipien lernen

**Für Datenstrategie:**
- Product Management lernen
- Change Management verstehen
- Leadership Skills entwickeln

---

## ✅ Self-Assessment

Rate dich selbst (1-5) in jeder Fähigkeit:

**Neugierde: ___ / 5**
- Stelle ich immer "Warum?"-Fragen?
- Grabe ich tiefer als Oberfläche?
- Hinterfrage ich Annahmen?

**Kontext: ___ / 5**
- Berücksichtige ich externe Faktoren?
- Verstehe ich das Business-Problem?
- Kenne ich die Industrie-Trends?

**Technische Herangehensweise: ___ / 5**
- Kann ich Probleme systematisch zerlegen?
- Teste ich Lösungen strukturiert?
- Dokumentiere ich meinen Ansatz?

**Datendesign: ___ / 5**
- Sind meine Strukturen klar und effizient?
- Sind meine Visualisierungen effektiv?
- Plane ich Datenarchitektur vorausschauend?

**Datenstrategie: ___ / 5**
- Manage ich Stakeholder gut?
- Habe ich klare Prozesse?
- Wähle ich die richtigen Tools?

---

*Aktualisiert: Oktober 2025*