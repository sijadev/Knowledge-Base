---
autor: Simon Janke
title: Datengestützte Modellauswahl
type: Google Data Analytics Kurs
date: 2025-10-25
tags:
  - "#datengestütze-modellauswahl"
  - data-analyze-prozess
links:
  - "[[Fragen für datengesteuerte Entscheidungsfindung]]"
---
---
**Der allgemeine Ansatz – 5 Schritte:**

**1. Das Problem verstehen (Problemdefinition)**

Zuerst musst du klar verstehen, was du lösen willst:

- Ist es eine Vorhersage? ("Wie viel Umsatz nächsten Monat?")
- Ist es eine Klassifizierung? ("Ist dieser Kunde ein VIP oder nicht?")
- Ist es eine Segmentierung? ("Welche Kundengruppen gibt es?")
- Ist es eine Optimierung? ("Wie maximiere ich den Gewinn?")

Das **Problem bestimmt die mathematische Form**!

---

**2. Explorative Datenanalyse (EDA)**

Du schaust dir die Daten an und fragst:

- Wie sehen die Daten aus? (Verteilung, Ausreißer, Muster)
- Welche Beziehungen gibt es zwischen den Variablen?
- Gibt es klare Trends oder Muster?

**Das zeigt dir**, welche mathematischen Formen passen könnten.

**Beispiele:**

- Wenn du ein lineares Muster siehst → **Lineare Regression** passt
- Wenn die Daten in Gruppen clustern → **Clustering-Algorithmen** passen
- Wenn es ein exponentielles Wachstum gibt → **Exponentielle Funktion** passt

---

**3. Domain-Expertise nutzen**

Du fragst Fachleute oder nutzt dein Wissen:

- "Welche mathematischen Modelle funktionieren typischerweise bei solchen Problemen?"
- "Was sagt die Theorie meines Fachbereichs?"

**Beispiele:**

- Verkaufsvorhersage: Erfahrene Verkäufer wissen oft, dass **saisonale Muster** wichtig sind
- Medizin: Ärzte wissen, dass bestimmte Prozesse **exponentiell** verlaufen
- Marketing: Profis wissen, dass Kundenverhalten oft **segmentiert** ist

---

**4. Hypothesen aufstellen und testen**

Du stellst Vermutungen auf und testest mehrere mathematische Formen:

````
Hypothese 1: "Der Umsatz wächst LINEAR mit der Werbeausgabe"
   → Teste: Lineare Regression y = a + b·x
   
Hypothese 2: "Der Umsatz wächst EXPONENTIELL mit der Werbeausgabe"
   → Teste: Exponentielles Modell y = a·e^(b·x)
   
Hypothese 3: "Der Umsatz wächst LOGARITHMISCH (mit abnehmender Steigerung)"
   → Teste: Logarithmisches Modell y = a + b·log(x)
```

Du führst jedes Modell durch und schaust, **welches die besten Ergebnisse liefert**.

---

**5. Modelle vergleichen und bewerten**

Du brauchst Kennzahlen (Metriken) um zu entscheiden, welche mathematische Form am besten passt:

**Häufige Bewertungs-Metriken:**
- **R² (Bestimmtheitsmaß):** Wie gut erklärt das Modell die Daten? (0-1, höher = besser)
- **RMSE (Root Mean Square Error):** Wie groß ist der durchschnittliche Fehler? (niedriger = besser)
- **MAE (Mean Absolute Error):** Wie weit liegen Vorhersagen im Schnitt daneben? (niedriger = besser)

---

**Praktisches Beispiel – Der komplette Prozess:**

**Szenario:** Du analyisierst, wie Kundenzufriedenheit von der Lieferzeit abhängt.

**Schritt 1 – Problem verstehen:**
"Ich will vorhersagen: Wie zufrieden ist ein Kunde bei X Tagen Lieferzeit?"

**Schritt 2 – Daten explorieren:**
```
Du zeichnest ein Streudiagramm:
Zufriedenheit
    100% |     ●
         |   ●   ●
         | ●       ●
         |●         ●
         |           ●
         └─────────────── Lieferzeit (Tage)
```
→ Das sieht LINEAR aus! Je länger die Lieferzeit, desto niedriger die Zufriedenheit.

**Schritt 3 – Domain-Expertise:**
Du fragst Kollegen: "Logisch – Kunden wollen schnell ihre Ware. Das sollte linear sein."

**Schritt 4 – Hypothesen testen:**
```
Modell 1 (Linear):     y = 100 - 5·x
Modell 2 (Exponentiell): y = 100·e^(-0.1·x)
Modell 3 (Quadratisch):  y = 100 - 2·x²
```

**Schritt 5 – Bewerten:**

Nach Berechnung:
- Modell 1 (Linear): R² = 0.89 ✓ Sehr gut!
- Modell 2 (Exponentiell): R² = 0.72 ✗ Weniger gut
- Modell 3 (Quadratisch): R² = 0.86 ✓ Gut, aber nicht besser

**Entscheidung:** Das **lineare Modell** ist die beste Wahl!

---

**Zusammenfassung – Der Ansatz:**
```
Problem definieren
        ↓
    EDA durchführen (Daten visualisieren & verstehen)
        ↓
    Domain-Expertise einbeziehen
        ↓
    Mehrere mathematische Modelle aufstellen & testen
        ↓
    Mit Metriken vergleichen (R², RMSE, MAE)
        ↓
    Beste mathematische Form auswählen
````

**Der wichtigste Punkt:**

Es ist **nicht willkürlich**! Du fragst nicht einfach "Welche Formel soll ich nehmen?" – du **folgst einem systematischen Prozess**, bei dem die Daten, das Problem und die Expertise dir zusammen zeigen, welche mathematische Form passt.

Das nennt man **"datengestützte Modellauswahl"** – die Daten führen dich zur richtigen Mathematik! 📊✨

---
