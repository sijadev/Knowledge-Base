# 📦 Modul 3: Richten Sie Ihre Data Analytics Toolbox ein

**Stand:** Oktober 2025  
**Aktualisiert mit 2025 Features**

---

## 🎯 Lernziele

In diesem Modul lernen Sie:

- Die wichtigsten Tools für Datenanalyse einzurichten und zu verwenden
- SQL-Grundlagen mit BigQuery zu meistern
- Spreadsheet-Funktionen für Analysen zu nutzen
- Die Integration von AI-Tools in Ihren Workflow

---

## 🛠️ Tool-Übersicht

### 1. Google Sheets / Excel

**Zweck:** Grundlegende Datenanalyse und -manipulation

**Kernfunktionen:**

- VLOOKUP / XLOOKUP
- Pivot-Tabellen
- Bedingte Formatierung
- Datenvalidierung
- Formeln und Funktionen

**2025 AI-Features:**

- Smart Fill für Mustererkennung
- Explore-Feature für automatische Insights
- Formelvorschläge durch AI

### 2. SQL & BigQuery

**Was ist BigQuery?**
BigQuery ist Googles vollständig verwaltetes, serverloses Data Warehouse, das
es ermöglicht, super-schnelle SQL-Abfragen mit der Verarbeitungsleistung der
Google-Infrastruktur auszuführen.

**Grundlegende SQL-Befehle:**

```sql
-- Daten abrufen
SELECT column1, column2
FROM dataset.table
WHERE condition
ORDER BY column1 DESC
LIMIT 100;

-- Daten aggregieren
SELECT
  category,
  COUNT(*) as count,
  AVG(price) as avg_price
FROM dataset.products
GROUP BY category
HAVING COUNT(*) > 10;

-- Tabellen verbinden
SELECT
  o.order_id,
  c.customer_name,
  o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
```text

**Neue BigQuery Features 2025:**

### Gemini in BigQuery

- **SQL Code-Vervollständigung:** Automatische Vorschläge beim Schreiben von Queries
- **Natürliche Sprache zu SQL:** Fragen in natürlicher Sprache eingeben und SQL-Code generieren lassen
- **Query-Optimierung:** AI-basierte Vorschläge zur Verbesserung der Query-Performance

**Aktivierung:**

1. BigQuery Console öffnen
2. Gemini-Features im Settings-Menü aktivieren
3. Bei Query-Eingabe Tab-Taste für Vorschläge nutzen

### 3. Tableau Public

**Installation:**

1. Download von [public.tableau.com](https://public.tableau.com)
2. Kostenlose Version für Lernzwecke
3. Verbindung zu verschiedenen Datenquellen möglich

**Grundlegende Visualisierungen:**

- Bar Charts
- Line Graphs
- Scatter Plots
- Heat Maps
- Dashboards

**Best Practices:**

- Weniger ist mehr - nicht überlasten
- Konsistente Farbschemata verwenden
- Interaktive Elemente einbauen
- Mobile-optimierte Ansichten erstellen

### 4. R & RStudio

**Installation:**
```r

# R von r-project.org installieren

# RStudio von rstudio.com installieren

# Wichtige Pakete installieren
install.packages("tidyverse")
install.packages("ggplot2")
install.packages("dplyr")
install.packages("readr")
```text

**Erste Schritte:**
```r

# Daten einlesen
library(readr)
data <- read_csv("datei.csv")

# Daten explorieren
head(data)
summary(data)
str(data)

# Einfache Visualisierung
library(ggplot2)
ggplot(data, aes(x = variable1, y = variable2)) +
  geom_point() +
  theme_minimal()
```text

---

## 🤖 AI-Integration in den Workflow

### 1. Datenbereinigung mit AI

**Automatische Fehlererkennung:**

- Inkonsistente Formatierungen
- Ausreißer-Identifikation
- Fehlende Werte-Muster

**Tools:**

- Google Sheets Smart Cleanup
- BigQuery Data Quality Rules
- Gemini-gestützte Vorschläge

### 2. Code-Generierung

**SQL mit Gemini:**
```text
Nutzer: "Zeige mir die Top 10 Kunden nach Umsatz im letzten Quartal"

Gemini generiert:
SELECT
  customer_id,
  customer_name,
  SUM(order_total) as total_revenue
FROM orders
WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 3 MONTH)
GROUP BY customer_id, customer_name
ORDER BY total_revenue DESC
LIMIT 10;
```text

### 3. Insights-Generierung

**Automatische Musterkennung:**

- Trend-Identifikation
- Anomalie-Erkennung
- Korrelationsanalyse

---

## 📊 Praktische Übungen

### Übung 1: BigQuery Setup

1. Google Cloud Console aufrufen
2. Neues Projekt erstellen
3. BigQuery aktivieren
4. Public Dataset laden (z.B., `bigquery-public-data`)

### Übung 2: Erste SQL-Abfrage
```sql
-- Nutze das öffentliche Dataset
SELECT
  name,
  state,
  population
FROM `bigquery-public-data.usa_names.usa_1910_2013`
WHERE year = 2010
  AND state = 'CA'
ORDER BY number DESC
LIMIT 20;
```text

### Übung 3: Datenvisualisierung

1. Daten aus BigQuery exportieren
2. In Tableau Public importieren
3. Dashboard mit 3 Visualisierungen erstellen
4. Auf Tableau Public veröffentlichen

---

## 🔧 Troubleshooting

### Häufige BigQuery-Probleme

**Problem:** "Quota exceeded"
**Lösung:** Free Tier Limits beachten (1 TB Query/Monat kostenlos)

**Problem:** "Permission denied"
**Lösung:** IAM-Berechtigungen prüfen, richtiges Projekt ausgewählt?

**Problem:** "Query zu langsam"
**Lösung:**

- WHERE-Klauseln nutzen
- LIMIT verwenden
- Partitionierte Tabellen nutzen

### R/RStudio-Probleme

**Problem:** "Package nicht gefunden"
**Lösung:** `install.packages("packagename")`

**Problem:** "Cannot allocate memory"
**Lösung:** Datensubset verwenden oder Cloud-basierte Lösung

---

## 📚 Weiterführende Ressourcen

### BigQuery

- [BigQuery Sandbox (kostenlos)](https://cloud.google.com/bigquery/docs/sandbox)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [BigQuery Best Practices](https://cloud.google.com/bigquery/docs/best-practices-performance-overview)

### Tableau

- [Tableau Learning](https://www.tableau.com/learn)
- [Makeover Monday](https://www.makeovermonday.co.uk/)

### R

- [R for Data Science](https://r4ds.had.co.nz/)
- [RStudio Cheatsheets](https://www.rstudio.com/resources/cheatsheets/)

---

## ✅ Checkliste für Modul 3

- [ ] Google Cloud Account erstellt
- [ ] BigQuery aktiviert und getestet
- [ ] Erste SQL-Queries ausgeführt
- [ ] Tableau Public installiert
- [ ] Erste Visualisierung erstellt
- [ ] R und RStudio installiert
- [ ] Tidyverse-Pakete installiert
- [ ] Gemini in BigQuery aktiviert
- [ ] AI-Features getestet

---

## 🎯 Nächste Schritte

Nach Abschluss dieses Moduls sollten Sie:

1. Komfortabel mit SQL-Grundlagen sein
2. Einfache Dashboards erstellen können
3. R-Grundlagen verstehen
4. AI-Tools in Ihren Workflow integriert haben

**Bereit für Modul 4:** Process Data from Dirty to Clean

---

*Tipp: Erstellen Sie ein eigenes "Sandbox"-Projekt zum Experimentieren mit allen Tools!*
