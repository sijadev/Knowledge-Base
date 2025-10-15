---
autor: Simon Janke
title: Data Analysis Process MOC
type: MOC
date: 2025-10-14
tags:
  - moc
  - datenanalyse-prozess
  - hub
links:
  - "[[Grundlagen]]"
---

# 📋 Data Analysis Process - Map of Content

> **Zentrale Übersicht über den kompletten Datenanalyse-Prozess**

---

## 🔄 Die 6 Phasen des Datenanalyse-Prozesses

### 1. 🎯 [[Fragephase|FRAGEN (Ask)]]
**Das Problem definieren und verstehen**

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM [[Fragephase]] OR outgoing([[Fragephase]])
WHERE file.name != "Fragephase"
SORT file.name ASC
```

**Kernaktivitäten:**
- [[Problemdefinition]]
- [[SMART-Fragen]]
- [[Stakeholder-Analyse]]
- [[Root Cause Analysis]]

---

### 2. 📦 [[Vorbereitungsphase|VORBEREITEN (Prepare)]]
**Daten sammeln und organisieren**

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM [[Vorbereitungsphase]] OR outgoing([[Vorbereitungsphase]])
WHERE file.name != "Vorbereitungsphase"
SORT file.name ASC
```

**Kernaktivitäten:**
- [[Vorbereitung - Auswahl der Daten]]
- Datenquellen identifizieren
- Datenschutz sicherstellen

---

### 3. 🧹 [[Verarbeitungsphase|VERARBEITEN (Process)]]
**Daten bereinigen und transformieren**

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM [[Verarbeitungsphase]] OR outgoing([[Verarbeitungsphase]])
WHERE file.name != "Verarbeitungsphase"
SORT file.name ASC
```

**Kernaktivitäten:**
- [[Process - Verarbeitung von Daten]]
- Datenbereinigung
- Validierung

---

### 4. 🔍 [[Analyse-Phase|ANALYSIEREN (Analyze)]]
**Erkenntnisse aus den Daten gewinnen**

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM [[Analyse-Phase]] OR outgoing([[Analyse-Phase]])
WHERE file.name != "Analyse-Phase"
SORT file.name ASC
```

**Kernaktivitäten:**
- [[Analyse der Daten]]
- [[Statistische Untersuchung von Daten]]
- Muster erkennen

---

### 5. 📊 [[Phase der Weitergabe|TEILEN (Share)]]
**Ergebnisse kommunizieren**

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM [[Phase der Weitergabe]] OR outgoing([[Phase der Weitergabe]])
WHERE file.name != "Phase der Weitergabe"
SORT file.name ASC
```

**Kernaktivitäten:**
- Visualisierungen erstellen
- Präsentationen vorbereiten
- Story erzählen

---

### 6. 🚀 [[Handlungsphase|HANDELN (Act)]]
**Empfehlungen umsetzen**

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM [[Handlungsphase]] OR outgoing([[Handlungsphase]])
WHERE file.name != "Handlungsphase"
SORT file.name ASC
```

**Kernaktivitäten:**
- Maßnahmen implementieren
- Ergebnisse überwachen
- Prozess optimieren

---

## 🧠 Unterstützende Konzepte

### Analytisches Denken
- [[Analytisches Denken]]
- [[Arten des Denkens]]
- [[Visualisierung]]
- [[Strategisches Denken]]
- [[Problemorientierung]]
- [[Korrelation]]

### Data-Driven Ansätze
- [[Data-Driven Decision Making]]
- [[Data Analytics Fähigkeiten]]

---

## 📚 Übergreifende Ressourcen

### Visualisierungen
```dataview
TABLE WITHOUT ID
  file.link as "Prozess-Übersichten"
FROM #visualisierung OR #prozess
WHERE contains(file.name, "Übersicht") OR contains(file.name, "Lebenszyklus")
SORT file.name ASC
```

**Wichtige Diagramme:**
- [[Datenanalyse-Prozess-Übersicht]]
- [[Lebenszyklus von Daten]]
- [[Datenperspektive (Daten Analyze Prozess )]]

---

## 🔗 Verbindungen zu anderen MOCs

- [[📊 Tools & Techniken MOC]]
- [[⚖️ Fairness & Ethics MOC]]
- [[📖 Grundlagen MOC]]

---

## 📈 Lernfortschritt

```dataview
TABLE WITHOUT ID
  file.link as "Progress-Notizen",
  date as "Datum"
FROM "6. Progress"
SORT date DESC
LIMIT 5
```

---

## 🎯 Quick Links

| Kategorie | Links |
|-----------|-------|
| **Prozess** | [[Datenanalyse-Prozess-Übersicht]] |
| **Lifecycle** | [[Lebenszyklus von Daten]] |
| **Thinking** | [[Analytisches Denken]] |
| **Tools** | [[Tools für Datenanalysen]] |
| **Fairness** | [[Fairness]] |

---

*Letzte Aktualisierung: 2025-10-14*
