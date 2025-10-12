---
autor: Simon Janke
title: Häufige Datenanalyse-Fehler
type: Ressource
date: 2025-10-12
tags:
  - fehler
  - pitfalls
  - antipatterns
  - lessons-learned
---

# ⚠️ Häufige Datenanalyse-Fehler & Wie man sie vermeidet

Ein umfassender Guide zu den klassischen Fallstricken in der Datenanalyse.

---

## 🔴 Kategorie 1: Statistische Fehler

### Fehler 1.1: Korrelation als Kausalität interpretieren

**❌ Der Fehler:**
```
Beobachtung: Eisverkäufe und Ertrinkungsunfälle korrelieren positiv

Falsche Schlussfolgerung:
"Eisverkäufe verursachen Ertrinken → Eisverkauf verbieten!"

Richtig:
Beide werden durch einen dritten Faktor (Sommer/Hitze) verursacht
```

**Reales Business-Beispiel:**
```
Daten zeigen: 
- Kunden mit Premium-Support haben 50% höhere Retention
- Manch manager: "Geben wir allen Premium-Support!"

ABER: Causation ≠ Correlation
- Premium-Kunden sind bereits high-value und engaged
- Support ist Korrelat, nicht Ursache der Retention
- Experiment nötig um Kausalität zu beweisen
```

**✅ So vermeiden:**
1. Immer fragen: "Könnte X auch Y verursachen?" (reverse causation)
2. "Gibt es einen dritten Faktor Z?"
3. Nur A/B-Tests oder kontrollierte Experimente beweisen Kausalität
4. Bei starker Korrelation: Hypothese bilden, dann testen

---

### Fehler 1.2: P-Hacking / Cherry Picking

**❌ Der Fehler:**
```
Analyst testet 20 verschiedene Hypothesen und berichtet nur die eine,
die p < 0.05 zeigt, ohne zu erwähnen, dass 19 andere tests durchgeführt wurden.

Bei 20 Tests mit α=0.05 erwarte ich 1 "false positive" by chance!
```

**Beispiel:**
```
Test 1: Mobile vs Desktop Conversion → p = 0.32 ❌
Test 2: iOS vs Android Conversion → p = 0.18 ❌
Test 3: Chrome vs Safari Conversion → p = 0.71 ❌
...
Test 15: Dienstag vs Donnerstag Conversion → p = 0.03 ✓

Report: "Dienstag hat signifikant höhere Conversion!"
(ohne die 14 failed tests zu erwähnen)
```

**✅ So vermeiden:**
1. **Pre-register** Hypothesen vor Analyse
2. **Bonferroni-Korrektur** bei multiple testing (p-Wert / Anzahl Tests)
3. Alle Tests dokumentieren, nicht nur signifikante
4. Replikation in neuen Daten

---

### Fehler 1.3: Simpson's Paradox ignorieren

**❌ Der Fehler:**
Ein Trend in aggregierten Daten kehrt sich um, wenn man nach Gruppen segmentiert.

**Klassisches Beispiel - Uni-Admission:**
```
Gesamt:
- 40% Männer zugelassen
- 30% Frauen zugelassen
→ "Bias gegen Frauen!"

Pro Department:
Dept A: 60% Männer, 70% Frauen zugelassen
Dept B: 20% Männer, 30% Frauen zugelassen

Problem: Frauen bewerben sich mehr bei Dept B (schwerer)
```

**Business-Beispiel:**
```
Gesamt: Kampagne A hat höhere Conversion als B

Aber segmentiert:
- Mobile: B besser als A
- Desktop: B besser als A

Erklärung: A bekommt mehr Desktop-Traffic (konvertiert generell besser)
```

**✅ So vermeiden:**
1. **Immer segmentieren** nach wichtigen Dimensionen
2. Confounding Variables identifizieren
3. Multivariate Analysis statt univariate

---

### Fehler 1.4: Zu kleine Stichproben

**❌ Der Fehler:**
```
A/B-Test mit 50 Nutzern pro Variante
→ 40% vs 30% Conversion
→ "Variante A gewinnt!"

ABER: Mit so wenig Daten ist das pure Zufallsschwankung
```

**Minimum Sample Sizes:**
```
Für aussagekräftige A/B-Tests:
- Conversion ~5%: >2000 pro Variante
- Conversion ~10%: >1000 pro Variante  
- Conversion ~25%: >400 pro Variante

Minimum für jede Analyse: >30 (Central Limit Theorem)
Besser: >100
Ideal: >1000
```

**✅ So vermeiden:**
1. **Sample Size Calculator** vor Test nutzen
2. Power Analysis durchführen
3. Mindestlaufzeit einhalten (1-2 Wochen für A/B-Tests)
4. Bei kleinen Samples: Vorsicht mit Schlussfolgerungen

---

### Fehler 1.5: Survivorship Bias

**❌ Der Fehler:**
Nur "Überlebende" analysieren und daraus Schlüsse ziehen.

**Klassisches Beispiel - WW2 Flugzeuge:**
```
Militär analysiert zurückgekehrte Flugzeuge
→ Beschädigungen an Flügeln und Rumpf
→ Vorschlag: Diese Bereiche verstärken

FEHLER: Die Flugzeuge mit Motor-Schäden sind NICHT zurückgekehrt!
→ Motoren müssen verstärkt werden
```

**Business-Beispiele:**
```
1. "Erfolgreiche Startups haben alle früh gepivoted"
   → Falsch: Du siehst nicht die, die gepivoted UND gescheitert sind
   
2. "Unsere besten Kunden nutzen alle Feature X"
   → Was ist mit Churn? Haben die auch Feature X genutzt?
   
3. "Nutzer die > 10 Sessions haben, werden loyal"
   → Reverse: Loyale Nutzer haben > 10 Sessions (nicht Kausalität)
```

**✅ So vermeiden:**
1. **Kontrolle für "Nicht-Überlebende"** (Churn, Failed Projects, etc.)
2. **Cohort-Analysen** (alle Nutzer tracken, nicht nur aktive)
3. Frage: "Wen sehe ich NICHT in den Daten?"

---

## 🟡 Kategorie 2: Datenqualitäts-Fehler

### Fehler 2.1: Garbage In, Garbage Out

**❌ Der Fehler:**
Analyse auf schmutzigen Daten ohne Validierung.

**Beispiele:**
```
1. Tracking-Fehler:
   - Event fired 3x statt 1x
   - → Revenue 3x überschätzt
   
2. Duplikate:
   - Gleicher User mit 5 IDs
   - → Unique Users 5x überschätzt
   
3. Fehlende Werte als 0:
   - NULL Revenue → 0
   - → Durchschnitt falsch berechnet
   
4. Typ-Fehler:
   - "123" (string) + "456" = "123456" statt 579
```

**✅ So vermeiden:**
1. **Data Quality Checks** IMMER first step:
   ```sql
   -- Duplikate check
   SELECT id, COUNT(*) 
   FROM table GROUP BY id HAVING COUNT(*) > 1;
   
   -- NULL check
   SELECT COUNT(*) AS nulls 
   FROM table WHERE important_field IS NULL;
   
   -- Outliers check
   SELECT MIN(value), MAX(value), AVG(value), STDDEV(value)
   FROM table;
   ```

2. **Profiling** vor Analyse
3. **Stichproben manuell prüfen**
4. **Validierung gegen bekannte Benchmarks**

---

### Fehler 2.2: Sampling Bias

**❌ Der Fehler:**
Stichprobe ist nicht repräsentativ für Population.

**Beispiele:**
```
1. Online-Survey Bias:
   - Nur tech-savvy Nutzer antworten
   - → Überschätzt digitale Affinität
   
2. Voluntary Response Bias:
   - Nur sehr zufriedene/unzufriedene antworten
   - → Extreme Meinungen überrepräsentiert
   
3. Time-of-Day Bias:
   - Analyse nur Workday-Daten
   - → Übersieht Weekend-Nutzer
   
4. Geographic Bias:
   - Test nur in US
   - → Nicht übertragbar auf Europa/Asia
```

**✅ So vermeiden:**
1. **Random Sampling** wo möglich
2. **Stratified Sampling** für wichtige Segmente
3. **Quotas** für Ausgewogenheit
4. **Weights** für Repräsentativität
5. Dokumentiere Sampling-Methode

---

### Fehler 2.3: Daten-Leakage

**❌ Der Fehler:**
Future Information in Training-Daten (bei ML-Modellen).

**Beispiel:**
```
Problem: Churn Prediction
Features: 
- Customer_ID
- Last_Login_Date  ← LEAKAGE!
- Support_Tickets
- Churned (Target)

Warum Leakage?
- Gechurnete Kunden haben natürlich kein recent Login
- Modell lernt: "Kein Login = Churn"
- ABER: In Produktion weiß ich nicht wer einloggen wird!
```

**✅ So vermeiden:**
1. **Temporal Validation**: Train auf Vergangenheit, test auf Zukunft
2. Nur Features nutzen, die **vor** Target bekannt sind
3. "Könnte ich diese Info zum Predictions-Zeitpunkt haben?"

---

## 🟠 Kategorie 3: Analyse-Design-Fehler

### Fehler 3.1: HARKing (Hypothesizing After Results are Known)

**❌ Der Fehler:**
Nach dem Sehen der Daten eine "Hypothese" formulieren, als wäre sie vor der Analyse erstellt worden.

**Beispiel:**
```
Analyst schaut Daten an:
"Oh, Mobile Conversion ist 10% niedriger!"

Report:
"Wir HYPOTHESIERTEN dass Mobile Conversion niedriger sei..."

Problem: Das ist keine echte Hypothese, sondern post-hoc Erklärung
```

**✅ So vermeiden:**
1. **Pre-register** Hypothesen
2. Exploratory vs. Confirmatory Analysis trennen
3. Transparent über Discovery vs. Validation

---

### Fehler 3.2: One-Size-Fits-All Metrics

**❌ Der Fehler:**
Gleiche Metrik für verschiedene Kontexte nutzen.

**Beispiele:**
```
1. "Average Revenue per User" (ARPU)
   Problem: 
   - Bei skewed distributions irreführend
   - Ein Whale-Kunde kann Durchschnitt verzerren
   Besser: Median + P90

2. "Average Session Duration"
   Problem:
   - Länger ≠ Besser
   - Support-Seiten: Lang = Problem findet keine Lösung
   - Content-Seiten: Lang = Engagement
   Besser: Kontext-spezifische Metriken

3. "Click-Through-Rate" (CTR)
   Problem:
   - Hohe CTR, aber keine Conversion
   - Clickbait performiert "gut"
   Besser: Multi-metric evaluation
```

**✅ So vermeiden:**
1. **North Star Metric** definieren (kontextabhängig)
2. **Counter-Metrics** für jede Primary-Metric
3. **Guardrail Metrics** für Qualität
4. Segmentierte Metriken

---

### Fehler 3.3: Comparing Apples to Oranges

**❌ Der Fehler:**
Unfairer Vergleich durch unterschiedliche Bedingungen.

**Beispiele:**
```
1. Zeitvergleich ohne Seasonality:
   "Dezember-Sales sind 200% höher als November!"
   → Natürlich wegen Weihnachten
   
2. Geo-Vergleich ohne Normalisierung:
   "USA hat 10x mehr Sales als Schweiz!"
   → Ja, aber 40x mehr Einwohner
   
3. Produkt-Vergleich mit unterschiedlichem Age:
   "Product A hat mehr Users als B"
   → A ist seit 5 Jahren live, B seit 2 Monaten
```

**✅ So vermeiden:**
1. **Like-for-like** Vergleiche
2. **Normalisierung** (per Capita, per Day, etc.)
3. **Cohort-Vergleiche** statt absolute
4. **Control für Confounders**

---

## 🔵 Kategorie 4: Kommunikations-Fehler

### Fehler 4.1: Fehlender Kontext

**❌ Der Fehler:**
Zahlen ohne Vergleichswerte präsentieren.

**Schlecht:**
```
"Wir haben 10.000 neue User!"
```

**Besser:**
```
"Wir haben 10.000 neue User:
- vs 8.000 letzten Monat (+25%)
- vs Target von 12.000 (-17%)
- vs Industry Growth von +15% (outperforming)
- Haupttreiber: Organic Search (+40%)
```

**✅ So vermeiden:**
Immer 3 Kontexte geben:
1. **Temporal**: vs Vorperiode
2. **Target**: vs Ziel/Benchmark
3. **Why**: Treiber der Veränderung

---

### Fehler 4.2: Überkomplizierte Visualisierungen

**❌ Der Fehler:**
```
- 15 Lines in einem Chart
- 3D Pie Charts
- Dual Axes mit unterschiedlichen Skalen
- Zu viele Farben
```

**✅ So vermeiden:**
1. **One Chart, One Message**
2. **Max 3-5 Series** in einem Chart
3. **Simple > Complex**
4. **Test**: "Kann jemand in 5 Sekunden verstehen?"

---

### Fehler 4.3: False Precision

**❌ Der Fehler:**
Zu viele Dezimalstellen suggerieren höhere Genauigkeit als existiert.

**Schlecht:**
```
"Conversion Rate ist 2.847291%"
```

**Besser:**
```
"Conversion Rate ist ~2.8%"
oder
"Conversion Rate ist 2.8% ± 0.3% (95% CI)"
```

**✅ So vermeiden:**
1. Runde auf **significant figures**
2. **Konfidenzintervalle** statt Punktschätzungen
3. "Approximately" / "About" / "~" nutzen

---

## 🟢 Kategorie 5: Business-Logic-Fehler

### Fehler 5.1: Optimierung der falschen Metrik

**❌ Der Fehler:**
Lokales Optimum statt globales.

**Beispiele:**
```
1. E-Commerce optimiert "Add to Cart" Rate
   → Nutzer adden, aber kaufen nicht
   → Revenue sinkt trotz höherer Cart-Rate
   
2. Content-Site optimiert "Time on Page"
   → Nutzer finden Info nicht → lesen länger
   → Schlechte UX, aber "gute" Metrik
   
3. Support optimiert "Ticket Close Rate"
   → Tickets schnell geschlossen ohne Lösung
   → Customer Satisfaction sinkt
```

**✅ So vermeiden:**
1. **End-to-End** Metriken priorisieren (Revenue, CSAT, Retention)
2. **Counter-Metrics** immer monitoren
3. **A/B Test** ganze Customer Journey
4. Qualitative Feedback zusätzlich zu Quantitative

---

### Fehler 5.2: Short-term vs Long-term Trade-off ignorieren

**❌ Der Fehler:**
Nur kurzfristige Gewinne optimieren, langfristige Schäden ignorieren.

**Beispiele:**
```
1. Aggressive Email-Kampagnen:
   Short-term: +20% Revenue
   Long-term: +50% Unsubscribes, Brand Damage
   
2. Discount-Strategie:
   Short-term: Mehr Sales
   Long-term: Kunden warten auf Discounts, Margin erodiert
   
3. Clickbait-Headlines:
   Short-term: Higher CTR
   Long-term: Lower Trust, Bounce Rate steigt
```

**✅ So vermeiden:**
1. **Leading vs Lagging** Indicators tracken
2. **Cohort-basierte** Long-term Metrics
3. **LTV-Modelle** statt nur Acquisition
4. **Brand Health** Metrics parallel

---

### Fehler 5.3: Ignoring Implementation Costs

**❌ Der Fehler:**
Empfehlungen ohne Kosten-Nutzen-Analyse.

**Beispiel:**
```
Analyst: "Wenn wir Ladezeit um 1s reduzieren, steigt Conversion um 2%!"

CEO: "Great! Wie?"

Analyst: "Ähm... komplettes Rewrite der Infrastruktur?"

→ 2% Conversion-Lift = $100k Revenue
→ Rewrite kostet $1M + 6 Monate
→ ROI negativ!
```

**✅ So vermeiden:**
1. **Impact vs Effort** Matrix
2. **Quick Wins** identifizieren
3. **Engineering-Input** vor Empfehlungen
4. **Phased Rollout** Optionen

---

## 🛠️ Best Practices: Fehler-Prävention

### 1. Pre-Analysis Checklist
```
□ Hypothese klar formuliert
□ Sample Size berechnet
□ Confounders identifiziert
□ Data Quality geprüft
□ Bias-Quellen berücksichtigt
□ Success Criteria definiert
```

### 2. During Analysis
```
□ Dokumentiere jeden Schritt
□ Stichproben manuell prüfen
□ Segmentierte Analysen
□ Sanity Checks (stimmen Totals?)
□ Peer Review Code/Queries
```

### 3. Post-Analysis
```
□ Results validieren (separate Dataset)
□ Alternative Erklärungen prüfen
□ Limitations dokumentieren
□ Confidence Levels angeben
□ Stakeholder-Feedback einholen
```

### 4. Communication
```
□ Kontext immer geben
□ Unsicherheit transparent machen
□ Visualisierungen simpel halten
□ Actionable Recommendations
□ Follow-up Plan definieren
```

---

## 📚 Lernressourcen

**Bücher:**
- "Naked Statistics" - Charles Wheelan
- "How to Lie with Statistics" - Darrell Huff
- "The Signal and the Noise" - Nate Silver

**Papers:**
- "Statistical Mistakes and How to Avoid Them" - Various

**Online:**
- [Calling Bullshit](https://callingbullshit.org/) - Course on Data Reasoning
- [Spurious Correlations](https://tylervigen.com/spurious-correlations) - Fun Examples

---

## ✅ Quick Reference Card

**Top 10 Fehler vermeiden:**
1. ✅ Korrelation ≠ Kausalität
2. ✅ Sample Size matters
3. ✅ Segmentiere immer
4. ✅ Check Data Quality first
5. ✅ Beware Survivorship Bias
6. ✅ Pre-register Hypothesen
7. ✅ Give Context
8. ✅ Monitor Counter-Metrics
9. ✅ Consider Long-term
10. ✅ Document Assumptions

**Frage bei jeder Analyse:**
- "Könnte das Zufall sein?"
- "Wen/Was sehe ich NICHT in den Daten?"
- "Gibt es alternative Erklärungen?"
- "Welche Annahmen mache ich?"
- "Wie robust ist meine Schlussfolgerung?"

---

*Aktualisiert: Oktober 2025*