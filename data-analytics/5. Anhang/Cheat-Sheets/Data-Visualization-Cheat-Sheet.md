---
autor: Simon Janke
title: Data Visualization Cheat Sheet
type: Ressource
date: 2025-10-12
tags:
  - visualisierung
  - charts
  - dashboard
  - tableau
  - cheat-sheet
---

# 📊 Data Visualization Cheat Sheet

Der ultimative Guide für effektive Datenvisualisierung.

---

## 🎯 Chart-Auswahl: Der richtige Typ für jeden Zweck

### Vergleichs-Charts

#### Balkendiagramm (Bar Chart)
**Wann nutzen:** Kategorien vergleichen
```
Perfekt für:
✓ Top 10 Produkte nach Umsatz
✓ Verkäufe pro Region
✓ Vergleich verschiedener Jahre

Varianten:
- Horizontal (besser für lange Labels)
- Vertical (klassisch)
- Grouped (mehrere Serien)
- Stacked (Teile eines Ganzen zeigen)
```

**Best Practices:**
- Sortiere Balken (höchste → niedrigste, oder alphabetisch)
- Starte Y-Achse bei 0
- Max. 10-12 Kategorien
- Verwende einheitliche Farben (außer bei Hervorhebung)

**Beispiel-Code (Tableau):**
```
Rows: Category
Columns: SUM(Sales)
Sort: Descending by Sales
```

#### Säulendiagramm (Column Chart)
**Wann nutzen:** Zeitverläufe mit diskreten Perioden
```
Perfekt für:
✓ Monatliche Verkäufe (12 Monate)
✓ Quartalsvergleich
✓ Jährliche Entwicklung
```

---

### Trend-Charts

#### Liniendiagramm (Line Chart)
**Wann nutzen:** Kontinuierliche Zeitreihen
```
Perfekt für:
✓ Tägliche Besucherzahlen
✓ Aktienkurse
✓ Temperaturverläufe
✓ Langfristige Trends

Nicht für:
✗ Kategorische Vergleiche
✗ Zu viele Lines (max. 3-5)
```

**Best Practices:**
- Eine Hauptlinie hervorheben (dicker/dunkler)
- Datenpunkte nur bei wenigen Punkten zeigen
- Beschriftung direkt am Ende der Linie (nicht in Legende)
- Y-Achse passend zum Datenbereich (muss nicht bei 0 starten)

#### Area Chart (Flächendiagramm)
**Wann nutzen:** Volumen über Zeit zeigen
```
Perfekt für:
✓ Kumulativer Umsatz
✓ Inventar-Level über Zeit
✓ Stacked: Anteilsentwicklung

VORSICHT: Kann irreführend sein (Fläche überbetont Unterschiede)
```

---

### Teil-vom-Ganzen-Charts

#### Kreisdiagramm (Pie Chart)
**Wann nutzen:** Anteile eines Ganzen (SPARSAM!)
```
NUR wenn:
✓ Max. 5-7 Segmente
✓ Prozentsätze sind wichtig
✓ Ein Segment soll hervorgehoben werden

Besser vermeiden wenn:
✗ Genaue Vergleiche nötig
✗ Mehr als 7 Segmente
✗ Ähnliche Werte (schwer zu unterscheiden)

Alternative: Horizontal Bar Chart!
```

**Wenn Pie, dann richtig:**
- Größtes Segment bei 12 Uhr starten
- Im Uhrzeigersinn absteigend
- Beschriftung direkt am Segment (nicht nur Legende)
- "Other" für kleine Segmente zusammenfassen

#### Treemap
**Wann nutzen:** Hierarchische Daten, viele Kategorien
```
Perfekt für:
✓ Produktkategorien und Subkategorien
✓ Budget-Allocation
✓ Website-Struktur Analyse
```

#### Waffle Chart
**Wann nutzen:** Alternative zu Pie für 100-Teile
```
Perfekt für:
✓ Prozentsätze visualisieren (1 Kästchen = 1%)
✓ Verständlicher als Pie
```

---

### Verteilungs-Charts

#### Histogramm
**Wann nutzen:** Verteilung numerischer Daten
```
Perfekt für:
✓ Altersverteilung von Kunden
✓ Einkommensverteilung
✓ Response Times

Zeigt:
- Shape (normal, skewed, bimodal)
- Spread (Streuung)
- Outliers
```

**Best Practices:**
- Bin-Größe sorgfältig wählen
- 5-20 Bins typischerweise
- X-Achse: Bins, Y-Achse: Frequenz

#### Box Plot
**Wann nutzen:** Verteilung vergleichen, Outliers zeigen
```
Perfekt für:
✓ Gehälter über Abteilungen
✓ Preise verschiedener Kategorien
✓ Performance-Metriken vergleichen

Zeigt:
- Median (Linie in Box)
- Q1 und Q3 (Box-Grenzen)
- Min/Max (Whiskers)
- Outliers (Punkte außerhalb)
```

#### Violin Plot
**Wann nutzen:** Wie Box Plot, aber mehr Details
```
Kombiniert:
- Box Plot Info
- Density Plot (zeigt Verteilungsform)
```

---

### Beziehungs-Charts

#### Streudiagramm (Scatter Plot)
**Wann nutzen:** Korrelation zwischen 2 Variablen
```
Perfekt für:
✓ Preis vs. Verkaufsmenge
✓ Werbeausgaben vs. ROI
✓ Größe vs. Gewicht

Kann zeigen:
- Positive Korrelation (↗)
- Negative Korrelation (↘)
- Keine Korrelation (verstreut)
- Outliers
- Cluster
```

**Enhancements:**
- Größe für 3. Variable (Bubble Chart)
- Farbe für Kategorien
- Trendlinie hinzufügen
- Quadranten für Segmentierung

#### Bubble Chart
**Wann nutzen:** 3-4 Dimensionen zeigen
```
X-Achse: Variable 1
Y-Achse: Variable 2
Größe: Variable 3
Farbe: Variable 4 (optional)

Beispiel:
X: Werbeausgaben
Y: Umsatz
Größe: Kundenanzahl
Farbe: Region
```

---

### Geografische Charts

#### Choropleth Map (Farbkarte)
**Wann nutzen:** Werte über geografische Regionen
```
Perfekt für:
✓ Verkäufe pro Bundesland
✓ Bevölkerungsdichte
✓ Election Results
```

**Best Practices:**
- Sequentielle Farbskala (hell → dunkel)
- Farben für Farbblinde geeignet
- Normalisierung beachten (absolute vs. relative Zahlen)

#### Symbol Map (Punkt-Karte)
**Wann nutzen:** Exakte Locations wichtig
```
Perfekt für:
✓ Store Locations
✓ Delivery-Zonen
✓ Individual Transactions

Symbol-Größe kann Metrik repräsentieren
```

---

### Ranking & Comparison

#### Bullet Chart
**Wann nutzen:** Performance vs. Target
```
Perfekt für:
✓ KPI Dashboards
✓ Ziel vs. Ist-Vergleich
✓ Performance Ranges

Zeigt:
- Aktueller Wert (Balken)
- Target (Linie)
- Bereiche (gut/mittel/schlecht)
```

#### Lollipop Chart
**Wann nutzen:** Wie Bar, aber cleaner
```
Alternative zu Bar Chart:
- Weniger Tinte/Pixel
- Fokus auf Wert (Punkt)
- Moderner Look
```

---

### Zeitbasierte Special Charts

#### Gantt Chart
**Wann nutzen:** Zeitplan-Visualisierung
```
Perfekt für:
✓ Projekt-Timeline
✓ Ressourcen-Planung
✓ Task-Abhängigkeiten
```

#### Calendar Heatmap
**Wann nutzen:** Aktivität über Zeit + Muster
```
Perfekt für:
✓ GitHub Contributions
✓ Website-Traffic Muster
✓ Tägliche Aktivitäten
```

---

## 🎨 Farben: Die Psychologie & Best Practices

### Farbschemata

#### 1. Sequentiell (Single Hue)
**Wann:** Quantitative Daten, eine Variable
```
Hell → Dunkel
Beispiel: Umsatz (niedrig → hoch)

Gut für:
✓ Heatmaps
✓ Choropleths
✓ Single-metric ranges
```

#### 2. Divergierend (Two Hues)
**Wann:** Daten mit Mittelpunkt
```
Negativ ← Neutral → Positiv
Rot ← Weiß → Grün

Gut für:
✓ Profit/Loss
✓ Abweichungen vom Durchschnitt
✓ Sentiment (neg/pos)
```

#### 3. Kategorial (Distinct Colors)
**Wann:** Ungeordnete Kategorien
```
Unterschiedliche Farbtöne
Beispiel: Produkte, Regionen

Gut für:
✓ Line Charts (verschiedene Serien)
✓ Grouped Bars
✓ Scatter (Gruppen)
```

### Farb-Best-Practices

```
✅ DO:
- Max. 5-7 Farben in einer Visualisierung
- Konsistenz (gleiche Farbe = gleiche Bedeutung)
- Kontrast für Lesbarkeit
- Colorblind-friendly Paletten
- Grau für Kontext/Vergleichswerte
- Farbe sparsam für Emphasis

❌ DON'T:
- Rote/grüne Kombination (8% männlich colorblind)
- Zu viele bunte Farben (wirkt unprofessionell)
- Farbe ohne Bedeutung
- Zu helle/zu dunkle Farben
- Neon-Farben
```

### Empfohlene Farbpaletten

**Professional:**
- Tableau Default (colorblind-friendly)
- ColorBrewer (wissenschaftlich getestet)
- Material Design Colors

**Emotional Associations:**
```
Blau:   Vertrauen, Stabilität, Professionalität
Grün:   Wachstum, Erfolg, Positiv
Rot:    Warnung, Dringend, Negativ
Orange: Energie, Action, Aufmerksamkeit
Grau:   Neutral, Kontext, Benchmark
```

---

## 📏 Layout & Composition

### Dashboard-Layout Prinzipien

#### 1. F-Pattern (West Reading Culture)
```
Top-left: Wichtigste Info
Top-right: Sekundäre Info
Left side: Navigation/Filter
Center: Hauptvisualisierung
```

#### 2. Z-Pattern
```
Top-left → Top-right
  ↓          ↓
Bottom-left → Bottom-right
```

#### 3. Visual Hierarchy
```
Level 1: KPIs / Headlines (groß, oben)
Level 2: Main Charts (mittel, zentral)
Level 3: Details / Filters (klein, Seite)
```

### Grid System
```
✓ Verwende Grid für Alignment
✓ Konsistente Abstände (z.B. 8px-Grid)
✓ Charts gleicher Größe für Vergleichbarkeit
✓ Whitespace für Gruppierung
```

### Responsive Design
```
Überlege für verschiedene Screens:
- Desktop: Viele Details, multi-column
- Tablet: Reduzierte Details, 2-column
- Mobile: Essential KPIs only, single-column
```

---

## 📊 Chart-Spezifische Best Practices

### Achsen

```
✅ Y-Achse:
- Bei 0 starten für Mengen/Counts
- Kann bei anderen Werten starten für Trends
- Beschriftung klar und lesbar
- Einheiten angeben (€, %, kg)

✅ X-Achse:
- Zeitangaben vollständig (nicht "Jan" ohne Jahr)
- Bei vielen Kategorien: überlegen ob horizontal besser
- Sortierung logisch (chronologisch oder nach Wert)

❌ Vermeiden:
- Doppelte Y-Achsen (verwirrend!)
- Zu viele Gridlines
- 3D-Effekte (verzerrt Wahrnehmung)
```

### Titel & Labels

```
✅ Gute Titel:
- Actionable: "Q3 Sales Down 15% - Action Needed"
- Nicht nur: "Q3 Sales"

✅ Achsenbeschriftungen:
- "Monthly Revenue (in €1000)"
- Nicht nur: "Revenue"

✅ Datenlabels:
- Nur bei wichtigen Punkten
- Nicht überladen (max. 5-10 Labels)
- Positionierung überschneidet nicht

✅ Annotations:
- Markiere wichtige Events
- Erkläre Anomalien
- "Black Friday" bei Peak
```

### Legends

```
✅ DO:
- Direkt beim Chart (nicht weit weg)
- Noch besser: Direct labeling (Label direkt an Line)
- Alphabetisch oder nach Wert sortieren

❌ DON'T:
- Zu viele Einträge (> 7)
- Weit weg vom Chart positionieren
- Unlogische Reihenfolge
```

---

## 🎯 Dashboard Design

### KPI Design

```
Struktur eines guten KPI-Tiles:

┌─────────────────────────┐
│ Revenue                 │ ← Label
│                         │
│      €1.2M             │ ← Hauptwert (groß)
│                         │
│  ↑ 15% vs Last Month   │ ← Kontext/Vergleich
│                         │
│  [Mini Sparkline]      │ ← Trend (optional)
└─────────────────────────┘
```

**Farb-Coding:**
- Grün: Positiv / Ziel übertroffen
- Gelb: Warning / Nahe am Ziel
- Rot: Alert / Unter Ziel

### Dashboard-Typen

#### 1. Executive Dashboard
```
Ziel: High-level Overview
Elemente:
- 4-6 Key KPIs (groß)
- 2-3 High-level Charts
- Trend-Indikatoren
- Minimal Details

Refresh: Real-time oder täglich
```

#### 2. Operational Dashboard
```
Ziel: Tägliche Monitoring
Elemente:
- Real-time Daten
- Alerts für Anomalien
- Drill-down zu Details
- Filters für Segmente

Refresh: Real-time
```

#### 3. Analytical Dashboard
```
Ziel: Deep-dive Analyse
Elemente:
- Viele Filter/Parameter
- Multiple Views
- Drill-down Hierarchien
- Vergleichs-Tools

Refresh: On-demand oder scheduled
```

---

## ⚠️ Häufige Fehler & Fixes

### Fehler 1: Chart Junk
```
❌ Problem:
- Zu viele Dekorationen
- Unnecessary 3D effects
- Overwhelming colors

✅ Fix:
- Minimalistisch
- Fokus auf Daten
- Data-Ink Ratio maximieren
```

### Fehler 2: Falsche Charttypen
```
❌ Problem:
- Pie für viele Kategorien
- Line für kategorische Daten
- Bar ohne bei 0 zu starten

✅ Fix:
- Chart-Auswahl-Matrix verwenden
- "Would I understand this in 5 seconds?"
```

### Fehler 3: Inkonsistente Formate
```
❌ Problem:
- Verschiedene Datumsformate
- Inkonsistente Farben
- Wechselnde Metriken-Namen

✅ Fix:
- Style Guide erstellen
- Templates verwenden
- Naming Conventions
```

### Fehler 4: Zu viel auf einmal
```
❌ Problem:
- 20 Charts auf einer Seite
- Information Overload
- Keine klare Message

✅ Fix:
- "One dashboard, one story"
- Progressive Disclosure (Summary → Details)
- Max. 5-7 Charts pro View
```

### Fehler 5: Fehlender Kontext
```
❌ Problem:
- Zahlen ohne Vergleich
- Keine Benchmarks
- Keine Zeitdimension

✅ Fix:
- Immer Kontext geben:
  - vs. Last Period
  - vs. Target
  - vs. Benchmark
```

---

## 🛠️ Tools-Spezifische Tipps

### Tableau

```
Best Practices:
✓ Calculated Fields gut benennen
✓ Sets für dynamische Segmente
✓ Parameters für User-Interaktion
✓ Actions für Drill-down
✓ Dashboard Actions für Filtering

Performance:
- Extracts statt Live für große Datenmengen
- Aggregierte Daten bevorzugen
- Context Filters strategisch nutzen
```

### Google Looker Studio

```
Best Practices:
✓ Blended Data für Joins
✓ Berechnete Felder für Transformationen
✓ Date Range Controls für Flexibilität
✓ Filter für Interaktivität

Limitations beachten:
- Keine komplexen Calculated Fields
- Performance bei großen Datasets
```

### Excel/Google Sheets

```
Visualisierung:
✓ Sparklines für Trends in Tabellen
✓ Conditional Formatting als Heatmap
✓ SMALL/LARGE für dynamische Charts
✓ Named Ranges für Updates

Limitations:
- Nicht für komplexe Interaktivität
- Updates manuel
```

---

## 📚 Weiterführende Ressourcen

**Bücher:**
- "The Visual Display of Quantitative Information" - Edward Tufte
- "Storytelling with Data" - Cole Nussbaumer Knaflic
- "Information Dashboard Design" - Stephen Few

**Websites:**
- [Tableau Public Gallery](https://public.tableau.com/gallery/)
- [Information is Beautiful](https://informationisbeautiful.net/)
- [Storytelling with Data Blog](https://www.storytellingwithdata.com/)

**Tools für Inspiration:**
- [Observable](https://observablehq.com/)
- [D3 Gallery](https://d3js.org/)
- [Datawrapper](https://www.datawrapper.de/)

---

## ✅ Visualization Checklist

Vor dem Veröffentlichen prüfen:

**Daten:**
- [ ] Daten sind aktuell
- [ ] Keine Nullwerte/Fehler
- [ ] Aggregationen korrekt

**Design:**
- [ ] Richtiger Chart-Typ gewählt
- [ ] Farben konsistent und sinnvoll
- [ ] Text lesbar (Größe, Kontrast)
- [ ] Keine Chart Junk

**Kontext:**
- [ ] Titel aussagekräftig
- [ ] Achsen beschriftet mit Einheiten
- [ ] Quellen angegeben
- [ ] Zeitraum klar

**Accessibility:**
- [ ] Colorblind-friendly
- [ ] Text lesbar (min. 12pt)
- [ ] Tooltips für Details

**Story:**
- [ ] Klare Message
- [ ] Call-to-Action (wenn relevant)
- [ ] Logischer Flow

---

*Aktualisiert: Oktober 2025*