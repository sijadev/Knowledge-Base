---
autor: Simon Janke
title: Data Analytics Glossar - Erweitert
type: Ressource
date: 2025-10-12
tags:
  - glossar
  - begriffe
  - definitionen
  - nachschlagewerk
---

# 📖 Data Analytics Glossar - Komplett

---

## A

### Aggregation
**Definition:** Das Zusammenfassen von Daten zu einer zusammenfassenden Statistik.  
**Beispiel:** Berechnung der durchschnittlichen Verkaufszahlen pro Monat.  
**SQL:** `SELECT AVG(sales) FROM orders GROUP BY month`

### Algorithm (Algorithmus)
**Definition:** Eine Schritt-für-Schritt-Anweisung zur Lösung eines Problems oder zur Durchführung einer Berechnung.  
**Beispiel:** Der Sortieralgorithmus, um Daten von klein nach groß zu ordnen.

### Analytics (Analytik)
**Definition:** Die systematische Untersuchung von Daten, um Muster zu erkennen und Erkenntnisse zu gewinnen.  
**Typen:**
- **Descriptive Analytics:** Was ist passiert?
- **Diagnostic Analytics:** Warum ist es passiert?
- **Predictive Analytics:** Was wird passieren?
- **Prescriptive Analytics:** Was sollten wir tun?

### API (Application Programming Interface)
**Definition:** Eine Schnittstelle, die es verschiedenen Softwareanwendungen ermöglicht, miteinander zu kommunizieren.  
**Beispiel:** Google Analytics API, um Daten programmatisch abzurufen.

### Attribution
**Definition:** Der Prozess, Wert oder Erfolg verschiedenen Touchpoints in einer Customer Journey zuzuordnen.  
**Beispiel:** First-Touch Attribution, Last-Touch Attribution, Multi-Touch Attribution.

---

## B

### Baseline
**Definition:** Ein Ausgangswert oder Referenzpunkt für Vergleiche.  
**Beispiel:** "Die Conversion-Rate vor der Änderung war 2,5% (Baseline)."

### Bias (Verzerrung)
**Definition:** Eine systematische Abweichung in Daten oder Analysen, die zu ungenauen Schlussfolgerungen führt.  
**Typen:**
- **Selection Bias:** Stichprobe ist nicht repräsentativ
- **Confirmation Bias:** Nur Daten suchen, die Hypothese bestätigen
- **Survivorship Bias:** Nur "Überlebende" betrachten

**Beispiel:** Nur zufriedene Kunden antworten auf Umfrage → Positivere Ergebnisse als Realität.

### BigQuery
**Definition:** Googles serverlose, hoch skalierbare Enterprise Data Warehouse-Lösung.  
**Features:** Petabyte-Skalierung, SQL-Abfragen, Machine Learning Integration.

### Business Intelligence (BI)
**Definition:** Technologien und Strategien zur Analyse von Geschäftsdaten, um bessere Entscheidungen zu treffen.  
**Tools:** Tableau, Looker, Power BI.

---

## C

### Cardinality (Kardinalität)
**Definition:** Die Anzahl einzigartiger Werte in einem Datenfeld.  
**Beispiel:** 
- Spalte "Land": 5 einzigartige Werte → Niedrige Kardinalität
- Spalte "Customer ID": 10.000 einzigartige Werte → Hohe Kardinalität

### Churn Rate (Abwanderungsrate)
**Definition:** Der Prozentsatz der Kunden, die innerhalb eines bestimmten Zeitraums das Produkt/die Dienstleistung nicht mehr nutzen.  
**Formel:** `Churn Rate = (Verlorene Kunden / Kunden zu Beginn) × 100%`  
**Beispiel:** 100 Kunden zu Beginn, 10 kündigen → Churn Rate = 10%

### Cleaning (Datenbereinigung)
**Definition:** Der Prozess, Fehler, Duplikate und Inkonsistenzen aus Daten zu entfernen.  
**Typische Aufgaben:**
- Entfernen von Duplikaten
- Korrektur von Tippfehlern
- Behandlung fehlender Werte
- Standardisierung von Formaten

### Cohort
**Definition:** Eine Gruppe von Benutzern, die ein gemeinsames Merkmal oder Erlebnis in einem bestimmten Zeitraum teilen.  
**Beispiel:** Alle Nutzer, die sich im Januar 2025 registriert haben (Januar-Cohort).

### Correlation (Korrelation)
**Definition:** Ein statistisches Maß für die Stärke der Beziehung zwischen zwei Variablen.  
**Wertebereich:** -1 (perfekt negativ) bis +1 (perfekt positiv), 0 = keine Korrelation  
**WICHTIG:** Korrelation ≠ Kausalität!

### CTE (Common Table Expression)
**Definition:** Eine temporäre benannte Ergebnismenge in SQL, die innerhalb einer Abfrage verwendet werden kann.  
**Syntax:** `WITH cte_name AS (SELECT ...) SELECT * FROM cte_name`

### CSV (Comma-Separated Values)
**Definition:** Ein Dateiformat, in dem Daten als Textdatei gespeichert werden, wobei Werte durch Kommas getrennt sind.  
**Beispiel:**
```csv
name,age,city
Anna,25,Berlin
John,30,London
```

---

## D

### Dashboard
**Definition:** Eine visuelle Darstellung wichtiger Metriken und KPIs auf einer einzigen Seite.  
**Zweck:** Schneller Überblick über den Geschäftszustand.  
**Tools:** Tableau, Looker Studio, Power BI.

### Data Governance
**Definition:** Die Gesamtverwaltung der Verfügbarkeit, Nutzbarkeit, Integrität und Sicherheit von Daten in einem Unternehmen.  
**Umfasst:** Datenqualität, Datenschutz, Compliance, Zugriffsrechte.

### Data Lake
**Definition:** Ein zentralisiertes Repository, das große Mengen strukturierter und unstrukturierter Daten im Rohformat speichert.  
**Unterschied zu Data Warehouse:** Data Lake = ungefiltert, Data Warehouse = strukturiert & verarbeitet.

### Data Lineage
**Definition:** Die Dokumentation der Herkunft, Bewegung und Transformation von Daten durch verschiedene Systeme.  
**Zweck:** Nachvollziehbarkeit und Qualitätssicherung.

### Data Mining
**Definition:** Der Prozess der Entdeckung von Mustern und Wissen aus großen Datenmengen.  
**Techniken:** Clustering, Klassifikation, Assoziationsregeln.

### Data Warehouse
**Definition:** Ein zentrales Repository strukturierter Daten aus verschiedenen Quellen, optimiert für Analyse und Reporting.  
**Beispiele:** BigQuery, Snowflake, Redshift.

### Dimension
**Definition:** Eine Kategorie beschreibender Informationen in einem Data Warehouse (z.B. Zeit, Ort, Produkt).  
**Beispiel:** In einer Verkaufstabelle: Produkt-Name, Kategorie, Region = Dimensionen.

### Dirty Data
**Definition:** Daten, die Fehler, Duplikate, fehlende Werte oder Inkonsistenzen enthalten.  
**Beispiel:** 
- "Deutschland", "germany", "DE" → Inkonsistente Schreibweisen
- Fehlende E-Mail-Adressen
- Duplikate

### Drill-Down
**Definition:** Der Prozess, von aggregierten Daten zu detaillierteren Daten zu navigieren.  
**Beispiel:** Jahresumsatz → Quartalsumsatz → Monatsumsatz → Tagesumsatz.

---

## E

### ETL (Extract, Transform, Load)
**Definition:** Ein Prozess, bei dem Daten aus Quellen extrahiert, transformiert und in ein Zielsystem geladen werden.  
**Beispiel:**
1. **Extract:** Daten aus CSV-Dateien, APIs, Datenbanken abrufen
2. **Transform:** Bereinigen, aggregieren, formatieren
3. **Load:** In Data Warehouse (z.B. BigQuery) laden

### EDA (Exploratory Data Analysis)
**Definition:** Die erste Phase der Datenanalyse, in der Daten untersucht werden, um Muster, Anomalien und Zusammenhänge zu entdecken.  
**Methoden:** Visualisierungen, Zusammenfassungsstatistiken, Korrelationsmatrizen.

---

## F

### Fact Table (Faktentabelle)
**Definition:** Die zentrale Tabelle in einem Data Warehouse, die quantitative Daten (Metriken) enthält.  
**Beispiel:** Verkaufstransaktionen mit Umsatz, Menge, Datum.

### Filter
**Definition:** Eine Methode, um nur bestimmte Datenzeilen basierend auf Bedingungen anzuzeigen.  
**SQL:** `WHERE country = 'Germany' AND sales > 1000`

---

## G

### Granularity (Granularität)
**Definition:** Die Detailebene von Daten.  
**Beispiel:**
- Hohe Granularität: Daten auf Transaktionsebene (jede einzelne Bestellung)
- Niedrige Granularität: Aggregierte Daten (monatlicher Gesamtumsatz)

---

## H

### Histogram
**Definition:** Ein Diagramm, das die Häufigkeitsverteilung numerischer Daten zeigt.  
**Zweck:** Verteilung und Muster in Daten visualisieren.

---

## I

### Index
**Definition:** Eine Datenstruktur in Datenbanken, die Abfragen beschleunigt.  
**Analogie:** Wie ein Stichwortverzeichnis in einem Buch.

### Inner Join
**Definition:** Eine SQL-Operation, die nur Zeilen zurückgibt, bei denen es eine Übereinstimmung in beiden Tabellen gibt.  
**Beispiel:** Nur Kunden MIT Bestellungen.

---

## J

### JOIN
**Definition:** Eine SQL-Operation zum Kombinieren von Zeilen aus zwei oder mehr Tabellen basierend auf einer verwandten Spalte.  
**Typen:** INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN.

---

## K

### KPI (Key Performance Indicator)
**Definition:** Eine messbare Metrik, die den Erfolg eines Unternehmens oder einer Aktivität anzeigt.  
**Beispiele:**
- Conversion Rate
- Customer Lifetime Value
- Churn Rate
- Monthly Recurring Revenue (MRR)

---

## L

### Left Join
**Definition:** Gibt alle Zeilen aus der linken Tabelle zurück und übereinstimmende Zeilen aus der rechten Tabelle.  
**Beispiel:** Alle Kunden, auch die ohne Bestellungen.

---

## M

### Machine Learning (ML)
**Definition:** Ein Bereich der KI, bei dem Algorithmen aus Daten lernen, ohne explizit programmiert zu werden.  
**Typen:**
- **Supervised Learning:** Mit gelabelten Daten (z.B. Klassifikation)
- **Unsupervised Learning:** Ohne Labels (z.B. Clustering)
- **Reinforcement Learning:** Lernen durch Trial & Error

### Metric (Metrik)
**Definition:** Eine quantitative Messung, die verwendet wird, um die Leistung zu verfolgen.  
**Beispiele:** Umsatz, Nutzeranzahl, Seitenaufrufe.

### Missing Data (Fehlende Daten)
**Definition:** Werte, die in einem Datensatz nicht vorhanden sind.  
**Behandlung:**
- Löschen (wenn wenige)
- Imputation (ersetzen mit Durchschnitt, Median, etc.)
- Als eigene Kategorie behandeln

---

## N

### Normalization (Normalisierung)
**Definition:** Der Prozess, Daten in einer Datenbank so zu organisieren, dass Redundanz reduziert wird.  
**Zweck:** Datenintegrität und Effizienz verbessern.

### NULL
**Definition:** Ein spezieller Wert in Datenbanken, der das Fehlen von Daten repräsentiert.  
**WICHTIG:** NULL ≠ 0, NULL ≠ leerer String

---

## O

### Outlier (Ausreißer)
**Definition:** Ein Datenpunkt, der signifikant von anderen Beobachtungen abweicht.  
**Beispiel:** In einer Liste von Gehältern: 30k, 35k, 32k, 500k ← Ausreißer  
**Behandlung:** Untersuchen (Fehler vs. echtes Signal), ggf. entfernen oder separat betrachten.

---

## P

### Pivot Table (Pivot-Tabelle)
**Definition:** Ein Werkzeug zur Zusammenfassung, Analyse und Exploration von Daten durch Umstrukturierung.  
**Verwendung:** In Excel/Sheets zum schnellen Gruppieren und Aggregieren.

### Primary Key (Primärschlüssel)
**Definition:** Eine Spalte (oder Kombination), die jede Zeile in einer Tabelle eindeutig identifiziert.  
**Beispiel:** Customer ID, Order ID.  
**Eigenschaften:** Einzigartig, nicht NULL.

---

## Q

### Query
**Definition:** Eine Anfrage an eine Datenbank, um bestimmte Daten abzurufen.  
**Beispiel:** `SELECT * FROM customers WHERE country = 'Germany'`

### Quartile
**Definition:** Werte, die einen geordneten Datensatz in vier gleiche Teile teilen.  
**Q1:** 25. Perzentil  
**Q2:** 50. Perzentil (Median)  
**Q3:** 75. Perzentil

---

## R

### R
**Definition:** Eine Open-Source-Programmiersprache speziell für statistische Berechnungen und Grafiken.  
**Stärken:** Statistische Modelle, Datenvisualisierung (ggplot2).

### Retention Rate (Bindungsrate)
**Definition:** Der Prozentsatz der Kunden, die über einen bestimmten Zeitraum aktiv bleiben.  
**Formel:** `Retention = (Kunden am Ende - Neue Kunden) / Kunden zu Beginn × 100%`

### RFM-Analyse
**Definition:** Eine Segmentierungsmethode basierend auf:
- **Recency:** Wie kürzlich hat der Kunde gekauft?
- **Frequency:** Wie oft kauft der Kunde?
- **Monetary:** Wie viel gibt der Kunde aus?

---

## S

### Schema
**Definition:** Die Struktur einer Datenbank, einschließlich Tabellen, Spalten und deren Beziehungen.  
**Beispiel:** 
```
customers (customer_id, name, email)
orders (order_id, customer_id, total)
```

### SQL (Structured Query Language)
**Definition:** Eine standardisierte Sprache zum Verwalten und Abfragen relationaler Datenbanken.  
**Hauptoperationen:** SELECT, INSERT, UPDATE, DELETE, JOIN, GROUP BY.

### Standard Deviation (Standardabweichung)
**Definition:** Ein Maß für die Streuung von Datenpunkten um den Mittelwert.  
**Interpretation:**
- Kleine Standardabweichung → Daten nahe am Durchschnitt
- Große Standardabweichung → Daten weit verstreut

### Subquery (Unterabfrage)
**Definition:** Eine SQL-Abfrage innerhalb einer anderen Abfrage.  
**Beispiel:**
```sql
SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders WHERE total > 1000);
```

---

## T

### Tableau
**Definition:** Eine führende Business Intelligence und Datenvisualisierungssoftware.  
**Stärken:** Interaktive Dashboards, einfache Drag-and-Drop-Oberfläche.

### Time Series (Zeitreihe)
**Definition:** Eine Sequenz von Datenpunkten, die über die Zeit geordnet sind.  
**Beispiel:** Tägliche Aktienkurse, monatliche Verkaufszahlen.  
**Analyse:** Trends, Saisonalität, Zyklen identifizieren.

---

## U

### Unique
**Definition:** Einzigartig, keine Duplikate.  
**SQL:** `SELECT DISTINCT country FROM customers`

---

## V

### Variance (Varianz)
**Definition:** Die durchschnittliche quadratische Abweichung vom Mittelwert.  
**Formel:** σ² = Σ(x - μ)² / n  
**Verhältnis:** Varianz = (Standardabweichung)²

### Visualization (Visualisierung)
**Definition:** Die grafische Darstellung von Daten zur besseren Verständlichkeit.  
**Typen:** Liniendiagramm, Balkendiagramm, Streudiagramm, Heatmap, etc.

---

## W

### WHERE
**Definition:** Eine SQL-Klausel zum Filtern von Zeilen basierend auf Bedingungen.  
**Beispiel:** `WHERE age >= 18 AND country = 'Germany'`

### Window Function
**Definition:** Eine SQL-Funktion, die Berechnungen über eine Menge von Zeilen durchführt, die mit der aktuellen Zeile verbunden sind.  
**Beispiele:** ROW_NUMBER(), RANK(), SUM() OVER(), LAG(), LEAD().

---

## Z

### Z-Score
**Definition:** Die Anzahl der Standardabweichungen, die ein Datenpunkt vom Mittelwert entfernt ist.  
**Formel:** z = (x - μ) / σ  
**Verwendung:** Outlier-Erkennung (|z| > 3 oft als Ausreißer).

---

## Häufig verwendete Abkürzungen

| Abkürzung | Bedeutung |
|-----------|-----------|
| AOV | Average Order Value |
| ARPU | Average Revenue Per User |
| CAC | Customer Acquisition Cost |
| CLV / LTV | Customer Lifetime Value |
| CPA | Cost Per Acquisition |
| CPC | Cost Per Click |
| CPM | Cost Per Mille (1000 Impressions) |
| CR | Conversion Rate |
| CTR | Click-Through Rate |
| DAU | Daily Active Users |
| GDPR | General Data Protection Regulation |
| MAU | Monthly Active Users |
| MoM | Month-over-Month |
| MRR | Monthly Recurring Revenue |
| NPS | Net Promoter Score |
| ROAS | Return on Ad Spend |
| ROI | Return on Investment |
| SaaS | Software as a Service |
| SQL | Structured Query Language |
| YoY | Year-over-Year |

---

## SQL-spezifische Begriffe

### DDL (Data Definition Language)
Befehle zur Definition der Datenbankstruktur: CREATE, ALTER, DROP

### DML (Data Manipulation Language)
Befehle zur Manipulation von Daten: SELECT, INSERT, UPDATE, DELETE

### ACID
Eigenschaften von Datenbanktransaktionen:
- **Atomicity:** Alles oder nichts
- **Consistency:** Daten bleiben konsistent
- **Isolation:** Transaktionen beeinflussen sich nicht
- **Durability:** Änderungen sind dauerhaft

---

*Aktualisiert: Oktober 2025*