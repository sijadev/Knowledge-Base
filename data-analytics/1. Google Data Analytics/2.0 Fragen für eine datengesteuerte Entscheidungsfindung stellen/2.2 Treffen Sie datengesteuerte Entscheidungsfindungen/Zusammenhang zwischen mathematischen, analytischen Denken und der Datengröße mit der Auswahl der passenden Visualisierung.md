---
autor: Simon Janke
title: Zusammenhang zwischen mathematischen, analytischen Denken und der Datengröße mit der Auswahl der passenden Visualisierung
type: Google Data Analytics Kurs
date: 2025-10-25
tags:
  - "#mathematisches-denken"
  - analytisches-denken
  - "#visualisierung"
links:
  - "[[Mathematisches Denken]]"
  - "[[Analytisches Denken]]"
  - "[[Fragen für datengesteuerte Entscheidungsfindung]]"
---
---

## Diese drei Dinge arbeiten zusammen:

**Mathematisches Denken** befähigt dich, Daten korrekt zu verarbeiten und zu berechnen. Es gibt dir die technische Grundlage:

- Wie berechne ich einen Durchschnitt, Prozentsatz oder Trend?
- Welche Formeln brauche ich?
- Sind meine Berechnungen präzise und logisch?

**Analytisches Denken** befähigt dich, die richtigen Fragen zu stellen und Muster zu erkennen:

- Was sind die wichtigsten Erkenntnisse?
- Welche Geschichte erzählen meine Daten?
- Was soll der Betrachter verstehen?

**Der Zusammenhang zur Visualisierung:**

Diese beiden Denkweisen bestimmen gemeinsam, **welches Tool du wählst**, weil sie dir zeigen, **was du kommunizieren musst**.

---

**Praktische Beispiele:**

Sagen wir, du analysierst Verkaufsdaten von 12 Monaten:

- **Mathematisches Denken:** "Ich berechne die monatlichen Umsätze und den Gesamttrend."
- **Analytisches Denken:** "Ich frage mich: Gibt es Monate mit höherem Umsatz? Gibt es ein Muster?"
- **Erkenntnis:** "Ja! Der Umsatz steigt von Januar bis Dezember kontinuierlich."
- **Visualisierungs-Entscheidung:** → Ein **Liniendiagramm** ist ideal, um diesen Trend zu zeigen!

---

Ein anderes Beispiel – Kundenverteilung nach Regionen:

- **Mathematisches Denken:** "Ich berechne den Umsatz pro Region in Prozent."
- **Analytisches Denken:** "Frage: Welche Region bringt den meisten Umsatz?"
- **Erkenntnis:** "Region A hat 45%, Region B 30%, Region C 25%"
- **Visualisierungs-Entscheidung:** → Ein **Balken- oder Kreisdiagramm** ist ideal!

---

**Das Zusammenspiel:**

```
Mathematisches Denken          Analytisches Denken
    (Präzision)                   (Einsicht)
         ↓                              ↓
    Korrekte Berechnung    +   Richtige Frage stellen
         ↓                              ↓
         ├─────────────────────────────┤
                        ↓
           Die richtige Visualisierung wählen
                        ↓
           Klare, aussagekräftige Grafik
```

**Warum ist das wichtig?**

Wenn du **nur mathematisch** denkst, könntest du korrekte, aber irrelevante Visualisierungen erstellen. Wenn du **nur analytisch** denkst, könntest du tolle Ideen haben, aber die Berechnungen könnten falsch sein. Zusammen ermöglichen sie dir, die **perfekte Balance** zu finden: präzise Daten, die eine klare Geschichte erzählen, in der besten visuellen Form.

Das ist die Kunst der Datenanalyse! 📊✨

---

### **Datenmenge verändert die gesamte Strategie**.

Hier ist der erweiterte Zusammenhang:

**Small Data vs. Big Data – Die Unterschiede:**

**Small Data:**

- Überschaubare Menge (hunderte bis wenige tausend Datensätze)
- Leicht zu handhaben und zu verstehen
- Beispiele: Verkäufe eines kleinen Shops, Schülernoten einer Klasse

**Big Data:**

- Riesige Menge (Millionen bis Milliarden Datensätze)
- Komplex, benötigt spezielle Technologien
- Beispiele: Google-Suchanfragen, Social-Media-Aktivitäten, Sensor-Daten

---

**Wie beeinflusst die Datenmenge dein Denken?**

### **Bei SMALL DATA**

Mathematisches Denken:

- Du kannst einfache Formeln und Funktionen nutzen (Excel, Google Sheets)
- Die Berechnungen sind schnell durchführbar
- Du siehst alle Details

Analytisches Denken:

- Du kannst tiefere, detailliertere Fragen stellen
- "Welche 5 Kunden brachten die meisten Umsatz?"
- "Was ist das Muster bei jedem einzelnen?"

Visualisierung:

- Einzelne Datenpunkte können sichtbar sein
- Tabellen sind oft sinnvoll
- Einfache Tools: Excel, Google Sheets, Power BI

---

### **Bei BIG DATA**

Mathematisches Denken:

- Du brauchst automatisierte Prozesse und Programmierung (Python, SQL)
- Du kannst nicht alle Details einzeln überprüfen
- Der Fokus liegt auf Aggregation und Mustern
- Beispiel: Statt 1 Million Kundendaten einzeln zu prüfen, berechnest du Segmente

Analytisches Denken:

- Deine Fragen müssen anders sein
- Statt "Details" fragst du nach Trends und Mustern
- "Welches Kundensegment ist am wertvollsten?"
- "Gibt es anomale Muster in den Daten?"

Visualisierung:

- Einzelne Datenpunkte verschwinden
- Aggregierte Daten sind wichtiger
- Tools brauchen mehr Power: Tableau, Apache Spark, Elasticsearch
- Visualisierungen sind oft einfacher, weil sie Millionen Punkte zu wenigen Insights zusammenfassen

---

**Das komplette Zusammenspiel:**

```
SMALL DATA:
┌─────────────────────────────────────────┐
│ Mathematisches Denken:                  │
│ - Einzelne Berechnungen möglich         │
│ - Detaillierte Formeln                  │
├─────────────────────────────────────────┤
│ Analytisches Denken:                    │
│ - Tiefe Fragen stellen                  │
│ - Einzelne Muster erkennen              │
├─────────────────────────────────────────┤
│ Tool-Wahl:                              │
│ → Excel, einfache Diagramme             │
│ → Alle Details sichtbar machen          │
└─────────────────────────────────────────┘

BIG DATA:
┌─────────────────────────────────────────┐
│ Mathematisches Denken:                  │
│ - Automatisierte Prozesse               │
│ - Aggregation & Programmierung          │
├─────────────────────────────────────────┤
│ Analytisches Denken:                    │
│ - Trends & Muster finden                │
│ - Große Muster erkennen                 │
├─────────────────────────────────────────┤
│ Tool-Wahl:                              │
│ → Python, SQL, Tableau                  │
│ → Millionen Punkte zusammenfassen       │
└─────────────────────────────────────────┘
```

**Praktische Beispiele zum Unterschied:**

**Small Data – Einzelner Online-Shop:**

- Mathematik: "Durchschnittlicher Warenkorbwert berechnen"
- Analytik: "Welche 3 Produkte kaufen Kunden zusammen?"
- Visualisierung: Tabelle mit allen Kombinationen
- Tool: Excel reicht aus

**Big Data – E-Commerce-Plattform mit 1 Millionen Kunden:**

- Mathematik: "Segmentierung mit Machine Learning durchführen"
- Analytik: "Welche Kundentypen kaufen zusammen?" (statt einzelner Kombinationen)
- Visualisierung: Heatmap mit Millionen Daten zu wenigen Farben komprimiert
- Tool: Braucht Python, Tableau, Big Data Technologien

---

### **Der wichtigste Punkt**

Bei **Small Data** kannst du detailliert sein. Bei **Big Data** musst du **abstrahieren und vereinfachen**. Das verändert nicht nur die Tools, sondern auch dein mathematisches und analytisches Denken komplett!

Bei Big Data fragst du nicht "Was ist mit Kunde #47385?" – das ist unmöglich. Du fragst "Welche 5% der Kunden sind am wertvollsten?" und visualisierst das in einer einfachen Grafik.

---
