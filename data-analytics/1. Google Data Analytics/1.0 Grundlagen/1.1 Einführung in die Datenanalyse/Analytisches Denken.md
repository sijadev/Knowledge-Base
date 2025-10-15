---
autor: Simon Janke
title: Analytisches Denken
type: Google Data Analytics Kurs
date: 2025-10-02
tags:
  - visualisierung
  - strategien
  - problemorientiert
  - korrelation
  - gesamt-bild_detailorientiertes-denken
  - arten-des-analytischen-denkens
  - bias-bewusstsein
links:
  - "[[Grundlagen]]"
  - "[[Arten des Denkens]]"
  - "[[Bias-Bewusstsein]]"
  - "[[Fairness]]"
---

## 🧠 Analytisches Denken - Die 5 Säulen

Analytisches Denken ist die Fähigkeit, komplexe Probleme systematisch zu zerlegen, Muster zu erkennen und datenbasierte Entscheidungen zu treffen.

---

## 1. 📊 Visualisierung

### Definition
Visualisierungen helfen Datenanalysten, Informationen effektiver zu verstehen und zu erklären.

### Warum wichtig?
- **Muster werden sofort sichtbar**: Was in 1000 Zeilen Daten verborgen ist, zeigt ein Diagramm in Sekunden
- **Kommunikation**: Stakeholder verstehen visuelle Darstellungen schneller
- **Entdeckung**: Anomalien und Trends fallen ins Auge

### Praktische Beispiele

#### Beispiel 1: Verkaufstrends
```
Rohdaten:
Jan: 10.000€, Feb: 12.000€, März: 11.500€, April: 15.000€

Als Liniendiagramm → Sofort erkennbar: Aufwärtstrend mit kleinem Rückgang im März
```

#### Beispiel 2: Kundenverteilung
```
Daten: 1000 Kunden in 5 Regionen

Als Kreisdiagramm → Sofort sichtbar: Region A macht 45% aus (Fokus!)
```

### Visualisierungstypen nach Zweck

| Zweck | Diagrammtyp | Wann nutzen |
|-------|-------------|-------------|
| Vergleich | Balkendiagramm | Kategorien vergleichen |
| Zeitverlauf | Liniendiagramm | Trends über Zeit |
| Teil-zu-Ganzes | Kreisdiagramm | Anteile zeigen |
| Verteilung | Histogramm | Häufigkeiten |
| Beziehung | Streudiagramm | Korrelationen |
| Geografisch | Heatmap/Karte | Regionale Daten |

### ⚠️ Häufige Visualisierungsfehler

- ❌ **3D-Effekte** ohne Mehrwert (verzerren Proportionen)
- ❌ **Zu viele Farben** (verwirrt statt klärt)
- ❌ **Falsche Achsenskalierung** (manipuliert Wahrnehmung)
- ❌ **Zu viele Daten** in einem Chart (Information Overload)

---

## 2. 🎯 Strategie

### Definition
Strategisches Denken hilft Datenanalysten zu erkennen, **was** sie mit den Daten erreichen wollen und **wie** sie es erreichen können.

### Die strategische Denkweise

1. **Zielsetzung**: Was ist das Endziel?
2. **Ressourcenplanung**: Welche Daten/Tools brauche ich?
3. **Priorisierung**: Was ist am wichtigsten?
4. **Qualitätssicherung**: Wie stelle ich sicher, dass die Daten nützlich sind?

### Praxisbeispiel: E-Commerce Analyse

**Situation:** Online-Shop hat sinkende Conversion-Rate

**Strategisches Vorgehen:**

```
1. Ziel definieren:
   → Conversion-Rate um 20% steigern innerhalb 3 Monaten

2. Datenquellen identifizieren:
   → Web-Analytics (Google Analytics)
   → Kundenumfragen
   → A/B-Test Ergebnisse
   → Heatmaps

3. Prioritäten setzen:
   → Fokus auf Checkout-Prozess (größter Impact)
   → Zweitens: Landing Pages
   → Drittens: Produktseiten

4. Qualitätskriterien:
   → Daten müssen letzten 6 Monate abdecken
   → Mindestens 10.000 User-Sessions
   → Mobile & Desktop getrennt analysieren
```

### Strategische Fragen

- "Welche Analyse hat den **größten Business Impact**?"
- "Wo investiere ich meine **begrenzte Zeit** am besten?"
- "Welche Daten sind **nice-to-have** vs. **must-have**?"

---

## 3. 🎪 Problemorientierung

### Definition
Probleme identifizieren, beschreiben und systematisch lösen. Das Problem bleibt während des gesamten Projekts im Fokus.

### Der problemorientierte Ansatz

#### 1. Problem identifizieren
**Nicht:** "Unsere Website ist schlecht"
**Sondern:** "Die Bounce-Rate auf der Produktseite ist 65% (Benchmark: 40%)"

#### 2. Problem beschreiben
```
Was? Hohe Bounce-Rate
Wo? Produktseiten
Wann? Seit Website-Relaunch vor 2 Monaten
Wer? Primär mobile Nutzer (75% Bounce)
Wie viel? 25% über Benchmark
```

#### 3. Root Cause Analysis (5 Warum-Methode)

**Beispiel:**
```
Problem: Bounce-Rate ist hoch

Warum? → Seite lädt langsam
Warum? → Bilder sind zu groß
Warum? → Keine Bildkomprimierung
Warum? → Entwickler-Team wusste nicht um Best Practices
Warum? → Keine Guidelines für Web-Performance

→ Lösung: Web-Performance Guidelines erstellen
```

### Praxisübung

**Situation:** Ein SaaS-Unternehmen verliert 30% seiner Neukunden nach dem ersten Monat.

**Aufgabe:** Wende die 5-Warum-Methode an, um zur Grundursache zu gelangen.

---

## 4. 🔗 Korrelation

### Definition
Korrelationen sind Beziehungen zwischen zwei oder mehr Variablen. Eine Korrelation zeigt **ob** Dinge zusammenhängen, aber nicht **warum**.

### ⚠️ WICHTIG: Korrelation ≠ Kausalität

**Korrelation:** Zwei Dinge treten gemeinsam auf
**Kausalität:** Ein Ding **verursacht** das andere

### Klassisches Fehlinterpretations-Beispiel

```
Beobachtung: 
- Eisverkäufe steigen
- Ertrinkungsunfälle steigen

Falsche Schlussfolgerung: 
❌ Eisverkäufe verursachen Ertrinkungsunfälle

Richtige Interpretation:
✅ Beide werden durch einen dritten Faktor verursacht: SOMMER/HITZE
```

### Korrelationstypen

#### Positive Korrelation
**Beide steigen gemeinsam**
- Mehr Werbebudget → Mehr Verkäufe
- Mehr Mitarbeiter → Mehr Produktivität (bis zu einem Punkt)

#### Negative Korrelation
**Eine steigt, andere fällt**
- Höhere Preise → Weniger Verkäufe
- Längere Ladezeit → Niedrigere Conversion

#### Keine Korrelation
**Kein erkennbarer Zusammenhang**
- Schuhgröße → Intelligenz
- Wochentag → Haarfarbe

### Korrelationsstärke messen

```
Korrelationskoeffizient (r):
-1.0 ← Perfekt negativ
-0.7 ← Stark negativ
-0.3 ← Schwach negativ
 0.0 ← Keine Korrelation
+0.3 ← Schwach positiv
+0.7 ← Stark positiv
+1.0 ← Perfekt positiv
```

### Praktisches Beispiel: E-Commerce

**Daten analysiert:**
- Produktbewertungen (1-5 Sterne)
- Verkaufszahlen

**Ergebnis:**
```
Korrelation: r = 0.82 (stark positiv)

Interpretation:
✅ Produkte mit höheren Bewertungen verkaufen sich besser
✅ Es besteht ein starker Zusammenhang
❌ Höhere Bewertungen VERURSACHEN nicht zwingend mehr Verkäufe
❓ Mögliche Gründe: 
   - Bessere Produkte → Höhere Bewertungen UND mehr Verkäufe
   - Mehr Verkäufe → Mehr Bewertungen → Soziale Bewährtheit
```

### Korrelation als "Detektor"

Korrelation hilft beim Entdecken von Mustern:
1. **Screene** viele Variablen auf Korrelationen
2. **Identifiziere** interessante Zusammenhänge
3. **Untersuche** dann die Kausalität durch:
   - A/B-Tests
   - Controlled Experiments
   - Weitere Analysen

---

## 5. 🔍 Gesamtbild- und Detailorientiertes Denken

### Die Doppelperspektive

**Top-Down (Gesamtbild → Details)**
- Start: 30.000 Fuß Perspektive
- Dann: Zoom in auf wichtige Bereiche

**Bottom-Up (Details → Gesamtbild)**
- Start: Einzelne Datenpunkte
- Dann: Aggregation zum großen Bild

### Der Top-Down Ansatz (Meistens effizienter)

#### Phase 1: Überblick verschaffen (Gesamtsystem)
```
Beispiel: E-Commerce Performance Analyse

1. Alle Hauptmetriken prüfen:
   - Gesamt-Revenue: -5%
   - Traffic: +10%
   - Conversion: -12%  ← HOTSPOT!
   - Warenkorb: -3%
   - AOV: +2%
```

#### Phase 2: Relevante Bereiche eingrenzen
```
Conversion ist das Problem (-12%)

Segmentierung:
- Desktop: -2% (ok)
- Mobile: -25%  ← HOTSPOT!
- Tablet: -5% (ok)

→ Problem ist MOBILE-SPEZIFISCH
```

#### Phase 3: Gezielt in die Tiefe gehen
```
Mobile Conversion-Problem

Detail-Analyse:
- Landing Page: ok
- Produktseiten: ok
- Checkout: -40%  ← HOTSPOT!

Checkout-Details:
- Schritt 1 (Adresse): ok
- Schritt 2 (Zahlung): -50%  ← ROOT CAUSE!

→ Mobile Zahlungs-UI ist das Problem
```

### Wann welcher Ansatz?

| Situation | Ansatz | Warum |
|-----------|--------|-------|
| Neue Datenquelle | Top-Down | Überblick gewinnen |
| Bekanntes Problem | Bottom-Up | Direkt zum Detail |
| Performance-Monitoring | Top-Down | Hotspots finden |
| Bug-Fixing | Bottom-Up | Spezifische Ursache |
| Explorative Analyse | Top-Down | Muster entdecken |
| Hypothese testen | Bottom-Up | Gezielt validieren |

### Praktische Anwendung: Dashboard-Design

**Top-Down Dashboard:**
```
Ebene 1: Executive Summary (1 Slide)
→ 3-5 Key Metrics
→ Rot/Gelb/Grün Status

Ebene 2: Kategorie-Drill-Down (3-5 Slides)
→ Detailmetriken pro Bereich
→ Trend-Charts

Ebene 3: Detail-Analysen (10+ Slides)
→ Granulare Daten
→ Nur bei Bedarf
```

### ✅ Best Practice: Pyramidenprinzip

```
1. Beginne mit der Kernbotschaft
   "Mobile Conversion ist um 25% gesunken"

2. Hauptgründe (3-5)
   - Zahlungs-UI Problem
   - Ladezeit-Probleme
   - UX-Bugs

3. Details (nur wenn nötig)
   - Spezifische Fehler
   - Technische Logs
   - User-Feedback
```

---

## 🎯 Zusammenfassung: Die 5 Säulen in Aktion

**Typisches Projekt-Szenario:**

1. **Strategie**: Ziel setzen & Datenquellen planen
2. **Problemorientierung**: Kernproblem klar definieren
3. **Gesamtbild**: Erst Overview, dann Drill-Down
4. **Korrelation**: Zusammenhänge identifizieren
5. **Visualisierung**: Erkenntnisse kommunizieren

---

## 📚 Weiterführende Links

- [[Arten des Denkens]]
- [[Data-Driven Decision Making]]
- [[Root Cause Analysis]]
- [[Visualisierungs-Best-Practices]]

---

## 🎯 Praxisaufgabe

**Szenario:** Ein Streaming-Service bemerkt, dass 40% der neuen Abonnenten nach dem ersten Monat kündigen.

**Aufgaben:**
1. Wende alle 5 Säulen des analytischen Denkens an
2. Erstelle einen Analyse-Plan
3. Welche Korrelationen würdest du untersuchen?
4. Wie würdest du Top-Down vorgehen?

---

*Aktualisiert: Oktober 2025*