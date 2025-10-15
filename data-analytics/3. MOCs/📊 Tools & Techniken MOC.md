---
autor: Simon Janke
title: Tools & Techniken MOC
type: MOC
date: 2025-10-14
tags:
  - moc
  - tools
  - techniken
  - hub
links:
  - "[[Grundlagen]]"
  - "[[Data Analysis Process MOC]]"
---

# 📊 Tools & Techniken - Map of Content

> **Zentrale Übersicht über alle Tools, Techniken und Best Practices für Datenanalyse**

---

## 🛠️ Core Tools Overview

### Haupt-Tools für Data Analytics
[[Tools für Datenanalysen]]
[[Das Wichtigste über die wichtigsten Daten-Tools]]

```dataview
TABLE WITHOUT ID
  file.link as "Tool-Dokumentation",
  tags as "Kategorien"
FROM #tools OR [[Tools für Datenanalysen]]
WHERE file.name != "Tools & Techniken MOC"
SORT file.name ASC
```

---

## 📋 Kategorie: Spreadsheets

### Excel / Google Sheets

**Cheat Sheet:**
[[Spreadsheets-Cheat-Sheet]]

**Kernfunktionen:**
- Pivot Tables
- VLOOKUP / INDEX-MATCH
- Conditional Formatting
- Formeln: AVERAGE(), MEDIAN(), STDEV()
- COUNTIF() für Häufigkeiten

**Anwendungsfälle:**
- Schnelle Datenexploration
- Ad-hoc Analysen
- Reporting
- Kleine bis mittlere Datensätze (<100k Zeilen)

**Best Practices:**
```dataview
LIST
FROM [[Spreadsheets-Cheat-Sheet]] OR [[Best-Practices]]
WHERE contains(file.outlinks, [[Spreadsheets-Cheat-Sheet]])
```

---

## 🗄️ Kategorie: SQL & Datenbanken

### SQL (Structured Query Language)

**Cheat Sheet:**
[[SQL-Cheat-Sheet]]

**Kernkonzepte:**
```sql
-- Basis-Operationen
SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY

-- Joins
INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN

-- Aggregationen
COUNT(), SUM(), AVG(), MIN(), MAX()

-- Window Functions
ROW_NUMBER(), RANK(), LAG(), LEAD()
```

**Erste Schritte:**
[[Erste Schritte mit SQL und Datenvisualisierung]]

**Übungen:**
```dataview
TABLE WITHOUT ID
  file.link as "SQL-Übung"
FROM "5. Anhang/Übungsaufgaben"
WHERE contains(file.name, "SQL")
SORT file.name ASC
```

**Anwendungsfälle:**
- Große Datenmengen (>100k Zeilen)
- Komplexe Joins
- Datenbereinigung
- ETL-Prozesse

---

## 📊 Kategorie: Datenvisualisierung

### Visualisierung Tools

**Cheat Sheet:**
[[Data-Visualization-Cheat-Sheet]]

**Haupt-Tools:**
- Tableau
- Power BI
- Google Data Studio
- Python (Matplotlib, Seaborn, Plotly)
- R (ggplot2)

**Visualisierungstypen:**

| Zweck | Chart-Typ | Wann nutzen |
|-------|-----------|-------------|
| Vergleich | Bar Chart | Kategorien vergleichen |
| Zeitverlauf | Line Chart | Trends über Zeit |
| Teil-zu-Ganzes | Pie Chart | Anteile zeigen |
| Verteilung | Histogram | Häufigkeiten |
| Beziehung | Scatter Plot | Korrelationen |
| Geografisch | Heat Map | Regionale Daten |

**Best Practices:**
```dataview
LIST
FROM [[Data-Visualization-Cheat-Sheet]] OR [[Visualisierungs-Best-Practices]]
SORT file.name ASC
```

---

## 🐍 Kategorie: Programmierung

### Python für Data Analytics

**Bibliotheken:**
- **Pandas**: Datenmanipulation
- **NumPy**: Numerische Berechnungen
- **Matplotlib/Seaborn**: Visualisierung
- **Scikit-learn**: Machine Learning
- **Jupyter Notebooks**: Interaktive Analyse

**Typischer Workflow:**
```python
# 1. Import
import pandas as pd

# 2. Daten laden
df = pd.read_csv('data.csv')

# 3. Exploration
df.info()
df.describe()

# 4. Cleaning
df.dropna()
df.drop_duplicates()

# 5. Analysis
df.groupby('category').mean()

# 6. Visualization
df.plot()
```

### R für Data Analytics

**Haupt-Packages:**
- **dplyr**: Datenmanipulation
- **ggplot2**: Visualisierung
- **tidyr**: Data Tidying
- **readr**: Daten Import

---

## 📈 Kategorie: Statistische Analysen

### Exploratory Data Analysis (EDA)

**[[Statistische Untersuchung von Daten]]**

**Standard-Workflow:**
```
Phase 1: Überblick verschaffen
Phase 2: Deskriptive Statistik
Phase 3: Datenqualität prüfen
Phase 4: Verteilungen verstehen
Phase 5: Beziehungen erkunden
```

**Minimum-Checks (IMMER):**
- [ ] Zeilen/Spalten zählen
- [ ] Datentypen prüfen
- [ ] Fehlende Werte checken
- [ ] Mean/Median für wichtige Variablen
- [ ] Duplikate suchen

**Tools für EDA:**
- Python: `df.describe()`, `df.info()`
- R: `summary()`, `str()`
- SQL: `COUNT()`, `AVG()`, `MIN()`, `MAX()`

---

## 🎯 Tool-Auswahl-Matrix

### Wann welches Tool?

```dataview
TABLE WITHOUT ID
  Datenmenge as "Datenmenge",
  Komplexität as "Komplexität",
  "Empfohlenes Tool" as Tool
FROM ""
WHERE file = this.file
FLATTEN [
  {Datenmenge: "< 10k Zeilen", Komplexität: "Einfach", Tool: "Excel/Sheets"},
  {Datenmenge: "< 10k Zeilen", Komplexität: "Mittel", Tool: "Excel + Python"},
  {Datenmenge: "10k - 1M Zeilen", Komplexität: "Einfach", Tool: "SQL"},
  {Datenmenge: "10k - 1M Zeilen", Komplexität: "Mittel-Hoch", Tool: "SQL + Python"},
  {Datenmenge: "> 1M Zeilen", Komplexität: "Beliebig", Tool: "SQL + Python/R"}
] as row
FLATTEN row.Datenmenge as Datenmenge
FLATTEN row.Komplexität as Komplexität
FLATTEN row.Tool as Tool
```

**Faustregel:**
- **Quick & Dirty**: Excel/Sheets
- **Mittelgroße Daten**: SQL
- **Komplexe Analysen**: Python/R
- **Business Dashboards**: Tableau/Power BI
- **Reproduzierbare Analysen**: Python/R (Notebooks)

---

## 📚 Cheat Sheets Übersicht

```dataview
TABLE WITHOUT ID
  file.link as "Cheat Sheet",
  date as "Erstellt"
FROM "5. Anhang/Cheat-Sheets"
SORT file.name ASC
```

### Quick Access
- [[SQL-Cheat-Sheet]]
- [[Data-Visualization-Cheat-Sheet]]
- [[Spreadsheets-Cheat-Sheet]]

---

## 🎓 Lernressourcen

### Toolbox Setup
[[Toolbox_Overview_2025]]

### Erste Schritte
[[Erste Schritte mit SQL und Datenvisualisierung]]

### Ressourcen-Sammlung
```dataview
TABLE WITHOUT ID
  file.link as "Ressource",
  tags as "Thema"
FROM "5. Anhang"
WHERE contains(file.name, "Ressourcen")
SORT file.name ASC
```

---

## 🔧 Best Practices nach Kategorie

### Datenbereinigung
[[Best-Practices]]

**Kernprinzipien:**
- Dokumentiere jeden Schritt
- Behalte Originaldaten
- Validiere nach jeder Transformation
- Nutze automatisierte Tests

### Datenvisualisierung
**Anti-Patterns vermeiden:**
- ❌ 3D-Charts ohne Mehrwert
- ❌ Zu viele Farben
- ❌ Falsche Achsenskalierung
- ❌ Chart Junk (unnötige Dekorationen)

**Pro-Tipps:**
- ✅ KISS: Keep It Simple, Stupid
- ✅ Farben mit Bedeutung nutzen
- ✅ Direkte Beschriftung (keine Legenden wenn möglich)
- ✅ Kontext durch Referenzlinien

### Code-Qualität
**Prinzipien:**
- DRY: Don't Repeat Yourself
- Funktionen für wiederverwendbaren Code
- Aussagekräftige Variablennamen
- Kommentare für komplexe Logik

---

## 🚀 Workflow-Templates

### Standard Data Analysis Workflow

```
1. 📥 Daten Import
   Tool: Python/R/SQL

2. 🔍 EDA (Exploratory Data Analysis)
   Tool: Jupyter Notebook / R Markdown

3. 🧹 Data Cleaning
   Tool: Python (Pandas) / SQL

4. 📊 Analysis
   Tool: Python/R + Visualization Library

5. 📈 Reporting
   Tool: Tableau/Power BI + Presentation

6. 🔄 Iteration
   Back to Step 2-5 as needed
```

### Quick Analysis Template
```python
# === 1. SETUP ===
import pandas as pd
import matplotlib.pyplot as plt

# === 2. LOAD ===
df = pd.read_csv('data.csv')

# === 3. EXPLORE ===
print(df.info())
print(df.describe())

# === 4. CLEAN ===
df = df.dropna()
df = df.drop_duplicates()

# === 5. ANALYZE ===
result = df.groupby('category')['value'].mean()

# === 6. VISUALIZE ===
result.plot(kind='bar')
plt.show()
```

---

## 🔗 Verbindungen

### Zu anderen MOCs
- [[📋 Data Analysis Process MOC]] - Wo Tools eingesetzt werden
- [[⚖️ Fairness & Ethics MOC]] - Ethischer Tool-Einsatz
- [[📖 Grundlagen MOC]] - Theoretische Basis

### Zu Praxis-Szenarien
```dataview
LIST
FROM "5. Anhang"
WHERE contains(file.name, "Praxis") OR contains(file.name, "Übung")
SORT file.name ASC
```

---

## 📝 Übungsaufgaben

```dataview
TABLE WITHOUT ID
  file.link as "Übung",
  tags as "Schwierigkeit"
FROM "5. Anhang/Übungsaufgaben"
SORT file.name ASC
```

---

## 🎯 Nächste Lernschritte

**Für Anfänger:**
1. Excel/Sheets Basics meistern
2. SQL Grundlagen lernen
3. Erste Visualisierungen in Tableau

**Für Fortgeschrittene:**
4. Python/R für Datenanalyse
5. Advanced SQL (Window Functions, CTEs)
6. Dashboard-Design

**Für Profis:**
7. Machine Learning Basics
8. Big Data Tools (Spark, etc.)
9. Cloud-Plattformen (AWS, GCP, Azure)

---

## 📊 Tool-Vergleichstabelle

| Feature | Excel | SQL | Python | R | Tableau |
|---------|-------|-----|--------|---|---------|
| Lernkurve | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Datenmenge | Klein | Groß | Groß | Groß | Groß |
| Visualisierung | ⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Reproduzierbarkeit | ⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Geschwindigkeit | ⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Kollaboration | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

*Letzte Aktualisierung: 2025-10-14*

---

> 💡 **Tool-Tipp:** Das beste Tool ist das, das du beherrschst UND das für dein Problem angemessen ist. Master one, learn others!
