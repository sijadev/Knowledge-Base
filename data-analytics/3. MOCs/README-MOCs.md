---
autor: Simon Janke
title: MOCs - Maps of Content
type: Documentation
date: 2025-10-14
tags:
  - readme
  - moc
  - documentation
---

# 📚 Maps of Content (MOCs) - Übersicht

## Was sind MOCs?

**Maps of Content** sind spezielle Notizen, die als **Navigationshubs** und **Übersichtsseiten** für thematisch zusammenhängende Notizen dienen.

### 🎯 Zweck von MOCs

MOCs helfen dir dabei:
- ✅ **Schnellen Überblick** über komplexe Themenbereiche zu bekommen
- ✅ **Zusammenhänge** zwischen Konzepten zu verstehen
- ✅ **Navigation** in großen Wissenssammlungen zu erleichtern
- ✅ **Struktur** in deine Notizen zu bringen, ohne starr hierarchisch zu sein
- ✅ **Einstiegspunkte** für verschiedene Themenbereiche zu schaffen

### 🔄 MOCs vs. Ordner vs. Tags

| Struktur-Element | Verwendung | Flexibilität |
|------------------|------------|--------------|
| **Ordner** | Physische Organisation | Starr (1 Ort) |
| **Tags** | Kategorisierung | Flexibel (mehrere Tags) |
| **MOCs** | Thematische Übersichten | Sehr flexibel (multiple Verbindungen) |

**Best Practice:** Nutze alle drei zusammen!
- Ordner: Grobe Struktur (Kurse, Projekte, etc.)
- Tags: Kategorien & Eigenschaften
- MOCs: Thematische Navigationshilfen

---

## 🗺️ Deine MOC-Struktur

### Master MOC
**[[🏠 Data Analytics Home - Master MOC]]**
- Zentrale Einstiegsseite
- Verlinkt zu allen Haupt-MOCs
- Quick Access zu wichtigsten Ressourcen

### Haupt-MOCs

#### 1. [[📋 Data Analysis Process MOC]]
**Fokus:** Der 6-Phasen-Prozess der Datenanalyse
- Fragen → Vorbereiten → Verarbeiten → Analysieren → Teilen → Handeln
- Alle prozessbezogenen Notizen
- Analytisches Denken

#### 2. [[⚖️ Fairness & Ethics MOC]]
**Fokus:** Bias-Bewusstsein und ethische Datenanalyse
- Fairness-Konzepte
- Bias-Typen und -Erkennung
- Best Practices & Checklisten
- Statistische Untersuchungen für Fairness

#### 3. [[📊 Tools & Techniken MOC]]
**Fokus:** Praktische Werkzeuge und Techniken
- SQL, Python, R
- Visualisierung (Tableau, etc.)
- Cheat Sheets
- Tool-Auswahl und -Vergleiche

---

## 📖 Wie nutze ich MOCs?

### Tägliche Nutzung

**Szenario 1: Ich starte ein neues Projekt**
```
1. Öffne: 🏠 Master MOC
2. Navigiere zu: 📋 Process MOC
3. Folge dem 6-Phasen-Prozess
4. Referenziere relevante Notizen
```

**Szenario 2: Ich will etwas über Fairness lernen**
```
1. Öffne: ⚖️ Fairness MOC
2. Durchstöbere die Konzepte
3. Nutze Dataview-Listen für verwandte Notizen
4. Folge den Links zu Detailnotizen
```

**Szenario 3: Ich suche ein Tool/Cheat Sheet**
```
1. Öffne: 📊 Tools MOC
2. Nutze Quick Links zu Cheat Sheets
3. Oder: Durchsuche Kategorien
```

### Wöchentliche Wartung

**MOCs aktuell halten:**
- [ ] Neue Notizen in relevante MOCs verlinken
- [ ] Dataview-Queries prüfen (funktionieren automatisch!)
- [ ] Neue Abschnitte hinzufügen bei neuen Themen

---

## 🔧 MOC-Techniken

### 1. Dataview-Integration

Alle MOCs nutzen Dataview für **automatische Aktualisierung**:

```dataview
LIST
FROM #fairness
WHERE file.name != "Fairness MOC"
SORT file.name ASC
```

**Vorteil:** Du musst nur die Original-Notiz mit Tags versehen, der MOC aktualisiert sich selbst!

### 2. Hierarchische Links

**Breadcrumb-Navigation** in MOCs:
```
🏠 Home > 📋 Process > Fragephase > Problemdefinition
```

### 3. Visual Aids

MOCs enthalten oft:
- Mermaid-Diagramme für Übersichten
- Tabellen für Vergleiche
- Checklisten für Workflows

---

## 💡 Best Practices für MOCs

### DO ✅

- **Kurze, prägnante Beschreibungen** in MOCs
- **Links zu Detailnotizen** statt alles im MOC
- **Dataview nutzen** für automatische Updates
- **Visuelle Elemente** (Emojis, Diagramme) für Orientierung
- **Regelmäßig reviewen** und aktualisieren

### DON'T ❌

- **Zu viel Content** direkt im MOC (besser: Links!)
- **Statische Listen** (nutze Dataview stattdessen)
- **Zu verschachtelt** (max. 2-3 Ebenen)
- **Duplikate** von Informationen aus anderen Notizen
- **"Tote Links"** (Links zu nicht existierenden Notizen)

---

## 🎯 MOC-Erweiterung

### Wann neue MOCs erstellen?

Erstelle einen neuen MOC wenn:
- ✅ Ein Thema 15+ Notizen umfasst
- ✅ Du häufig nach verwandten Notizen suchst
- ✅ Ein Themenbereich mehrere Unterthemen hat
- ✅ Andere MOCs zu groß werden (Split!)

### Mögliche zukünftige MOCs

Für später, wenn Themen wachsen:
- **SQL Deep Dive MOC** (wenn SQL-Notizen >20)
- **Statistics MOC** (bei statistischen Vertiefungen)
- **Project Portfolio MOC** (für abgeschlossene Projekte)
- **Career Development MOC** (Job-Suche, Interview-Prep)

---

## 🔍 MOC-Suche & Navigation

### In Obsidian

**Quick Switcher** (`Ctrl+O`):
```
moc          # Zeigt alle MOCs
home         # Direkt zum Master MOC
fairness     # Fairness MOC finden
```

**Graph View** (`Ctrl+G`):
- MOCs sind die großen "Hub"-Knoten
- Viele Verbindungen zu anderen Notizen
- Zentral im Graph positioniert

**Tag-Filter**:
```
tag:#moc     # Alle MOCs anzeigen
```

---

## 📊 MOC-Qualitätsmetriken

### Wie erkenne ich einen guten MOC?

**Checkliste:**
- [ ] Klare Struktur mit Überschriften
- [ ] Links zu 10+ relevanten Notizen
- [ ] Mindestens 1 Dataview-Query
- [ ] Visuelle Navigation (Emojis/Icons)
- [ ] Kurze Beschreibungen (1-2 Sätze)
- [ ] Links zu verwandten MOCs
- [ ] Aktualitätsdatum

### Deine aktuellen MOCs

```dataview
TABLE WITHOUT ID
  file.link as "MOC",
  date as "Erstellt",
  length(file.outlinks) as "Ausgehende Links",
  length(file.inlinks) as "Eingehende Links"
FROM "3. MOCs"
WHERE file.name != "README-MOCs"
SORT file.name ASC
```

---

## 🎓 Lernressourcen zu MOCs

### Weiterführende Infos

**Konzept-Erfinder:** Nick Milo (Linking Your Thinking)

**Empfohlene Lektüre:**
- [The MOC Method](https://www.youtube.com/c/NickMilo) - YouTube Channel
- [Building a Second Brain](https://www.buildingasecondbrain.com/) - Tiago Forte

---

## 🚀 Quick Start

**Neu hier? Start so:**

1. **Öffne:** [[🏠 Data Analytics Home - Master MOC]]
2. **Schaue dir** die Struktur an
3. **Folge Links** zu interessanten Themen
4. **Bookmarke** den Master MOC für schnellen Zugriff

**Keyboard-Shortcut-Tipp:**
Erstelle einen Custom Command in Obsidian:
```
Hotkey: Ctrl+H
Command: Open "Master MOC"
```

---

*Letzte Aktualisierung: 2025-10-14*

---

> 💡 **Denk dran:** MOCs sind lebende Dokumente. Sie entwickeln sich mit deiner Wissensbasis mit. Update sie regelmäßig, aber mach dir keinen Stress über Perfektion!
