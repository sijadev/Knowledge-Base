---
autor: Simon Janke
title: Data Analytics Best Practices
type: Ressource
date: 2025-10-12
tags:
  - best-practices
  - tipps
  - qualität
  - workflow
---

# 🌟 Data Analytics Best Practices

Ein umfassender Leitfaden für professionelle Datenanalyse.

---

## 🎯 1. Projektplanung & Fragestellung

### ✅ Best Practices

#### Klare Zielsetzung
```
❌ Schlecht: "Analysiere unsere Kundendaten"
✅ Gut: "Identifiziere die Top 3 Faktoren, die die Kundenabwanderung 
         im Q3 2025 beeinflusst haben, um Retention-Strategien zu entwickeln"
```

#### SMART-Fragen verwenden
- **S**pezifisch: Genau definiert
- **M**essbar: Quantifizierbar
- **A**ction-oriented: Führt zu Handlungen
- **R**elevant: Wichtig für Business
- **T**ime-bound: Zeitlich begrenzt

#### Stakeholder-Alignment
```
Vor Projektbeginn klären:
✓ Was ist das Geschäftsproblem?
✓ Wer sind die Stakeholder?
✓ Was sind die Erfolgskriterien?
✓ Welche Daten sind verfügbar?
✓ Was ist der Zeitrahmen?
✓ Wie werden Ergebnisse genutzt?
```

### ⚠️ Häufige Fehler vermeiden

```
❌ Direkt mit Datenanalyse beginnen ohne Kontext
❌ Lösungsorientiert statt problemorientiert denken
❌ Annahmen nicht dokumentieren
❌ Stakeholder-Erwartungen nicht managen
```

---

## 📊 2. Datensammlung & -vorbereitung

### ✅ Best Practices

#### Datenqualität prüfen
```python
# Checklist für neue Datenquellen:
✓ Vollständigkeit: Sind alle erwarteten Daten vorhanden?
✓ Genauigkeit: Sind die Werte korrekt?
✓ Konsistenz: Sind Formate einheitlich?
✓ Aktualität: Sind die Daten aktuell?
✓ Relevanz: Sind die Daten für die Fragestellung relevant?
```

#### Datenherkunft dokumentieren
```
Für jede Datenquelle festhalten:
- Quelle (z.B. Google Analytics, CRM-System)
- Extraktionsdatum
- Verantwortliche Person
- Bekannte Limitationen
- Transformationen angewendet
```

#### Backups erstellen
```
✓ Originaldaten NIEMALS überschreiben
✓ Versionierung verwenden (data_v1, data_v2)
✓ Transformation-Scripts speichern
```

### ⚠️ Häufige Fehler vermeiden

```
❌ Originaldaten überschreiben
❌ Keine Dokumentation der Bereinigungsschritte
❌ Bias in der Datensammlung ignorieren
❌ Stichproben ohne Repräsentativität prüfen
```

---

## 🧹 3. Datenbereinigung

### ✅ Best Practices

#### Systematischer Approach
```
1. Überblick verschaffen
   - Datentypen prüfen
   - Nullwerte identifizieren
   - Duplikate finden
   - Statistiken ansehen

2. Bereinigungsplan erstellen
   - Was wird bereinigt?
   - Wie wird es bereinigt?
   - Warum diese Methode?

3. Schrittweise bereinigen
   - Ein Problem nach dem anderen
   - Jeder Schritt dokumentiert
   - Ergebnisse validieren

4. Qualitätschecks
   - Vor/Nach-Vergleich
   - Stichproben prüfen
   - Edge Cases testen
```

#### Fehlende Daten behandeln
```
Strategien je nach Kontext:

✓ Löschen (wenn < 5% fehlen und zufällig)
✓ Imputation mit Durchschnitt/Median (bei numerisch)
✓ Most Frequent Value (bei kategoriell)
✓ Als eigene Kategorie "Unknown" (wenn Muster)
✓ Vorwärts-/Rückwärtsfüllen (bei Zeitreihen)

❌ NICHT einfach mit 0 ersetzen (verzerrt Statistiken)
```

#### SQL Best Practices für Cleaning
```sql
-- ✅ Gut: Explizit NULL-Handling
SELECT 
  customer_id,
  COALESCE(email, 'unknown@example.com') AS email,
  COALESCE(country, 'Unknown') AS country
FROM customers;

-- ✅ Gut: Duplikate identifizieren BEVOR löschen
SELECT email, COUNT(*) as count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;

-- ✅ Gut: Trimming und Case-Standardisierung
SELECT 
  TRIM(UPPER(country)) AS country_clean
FROM customers;
```

### ⚠️ Häufige Fehler vermeiden

```
❌ Fehlende Werte einfach mit 0 ersetzen
❌ Duplikate blind löschen (könnten legitim sein)
❌ Ausreißer automatisch entfernen (könnten wichtig sein)
❌ Datentypen nicht konvertieren (z.B. "123" als Text)
```

---

## 🔍 4. Explorative Datenanalyse (EDA)

### ✅ Best Practices

#### Start mit den Basics
```
1. Deskriptive Statistiken
   - Mittelwert, Median, Modus
   - Min, Max, Quartile
   - Standardabweichung

2. Verteilungen verstehen
   - Histogramme für numerisch
   - Balkendiagramme für kategoriell
   - Normal verteilt vs. skewed?

3. Beziehungen erkunden
   - Korrelationsmatrix
   - Scatterplots
   - Gruppenvergleiche
```

#### Visualisierung für Exploration
```
✓ Mehrere Darstellungen probieren
✓ Verschiedene Aggregationslevel
✓ Segmentierung nach wichtigen Dimensionen
✓ Zeitliche Trends untersuchen
✓ Outliers visuell identifizieren
```

#### Hypothesen bilden
```
Nach EDA solltest du haben:
1. Liste interessanter Muster
2. Vorläufige Hypothesen
3. Identifizierte Anomalien
4. Fragen für tiefere Analyse
```

### ⚠️ Häufige Fehler vermeiden

```
❌ Nur Durchschnitte betrachten (Verteilung wichtig!)
❌ Korrelation als Kausalität interpretieren
❌ Selection Bias nicht berücksichtigen
❌ Zeitliche Effekte ignorieren (Saisonalität)
```

---

## 📈 5. Datenanalyse & Statistik

### ✅ Best Practices

#### Statistisch korrekt denken
```
✓ Stichprobengröße berücksichtigen
  - n < 30: Vorsicht mit Durchschnitten
  - n > 1000: Auch kleine Effekte signifikant
  
✓ Konfidenzintervalle angeben
  "Conversion Rate ist 2,5% ± 0,3% (95% CI)"
  Nicht nur: "Conversion Rate ist 2,5%"

✓ P-Werte richtig interpretieren
  p < 0.05 bedeutet NICHT "Hypothese ist wahr"
  Es bedeutet: "Unwahrscheinlich durch Zufall"
```

#### A/B-Tests richtig durchführen
```
Vor dem Test:
✓ Hypothese klar formulieren
✓ Sample Size berechnen
✓ Randomisierung sicherstellen
✓ Laufzeit festlegen (min. 1 Woche)

Während des Tests:
✓ NICHT vorzeitig stoppen wenn "gut aussieht"
✓ Keine Änderungen am Test während Laufzeit
✓ Externe Faktoren dokumentieren

Nach dem Test:
✓ Statistische Signifikanz prüfen
✓ Praktische Signifikanz bewerten
✓ Segmentanalyse durchführen
✓ Langfristige Effekte monitoren
```

#### Segmentierung sinnvoll nutzen
```
✓ Nach sinnvollen Business-Dimensionen:
  - Kundentyp (B2B vs. B2C)
  - Region
  - Produktkategorie
  - Nutzungsverhalten

✓ Mindestgröße pro Segment beachten
  - Min. 100-500 Datenpunkte
  - Sonst: Zusammenfassen

✓ Simpson's Paradox beachten
  - Gesamttrend vs. Segmenttrends können gegensätzlich sein
```

### ⚠️ Häufige Fehler vermeiden

```
❌ Cherry-Picking: Nur positive Ergebnisse zeigen
❌ P-Hacking: Solange testen bis signifikant
❌ Multiple Testing ohne Korrektur
❌ Causation aus Correlation schließen
❌ Survivorship Bias (nur "Überlebende" analysieren)
```

---

## 💻 6. SQL Best Practices

### ✅ Best Practices

#### Lesbarkeit
```sql
-- ✅ Gut: Übersichtlich formatiert
SELECT 
  c.customer_id,
  c.name,
  COUNT(o.order_id) AS order_count,
  SUM(o.total_amount) AS total_spent
FROM customers c
LEFT JOIN orders o 
  ON c.customer_id = o.customer_id
WHERE o.order_date >= '2025-01-01'
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 5
ORDER BY total_spent DESC
LIMIT 100;

-- ❌ Schlecht: Alles in einer Zeile
SELECT c.customer_id,c.name,COUNT(o.order_id),SUM(o.total_amount) FROM customers c LEFT JOIN orders o ON c.customer_id=o.customer_id WHERE o.order_date>='2025-01-01' GROUP BY c.customer_id,c.name HAVING COUNT(o.order_id)>5 ORDER BY 4 DESC LIMIT 100;
```

#### Performance-Optimierung
```sql
-- ✅ Gut: Filter VOR JOIN
SELECT c.name, o.total
FROM (
  SELECT * FROM customers WHERE country = 'Germany'
) c
JOIN orders o ON c.customer_id = o.customer_id;

-- ❌ Langsam: Filter NACH JOIN
SELECT c.name, o.total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.country = 'Germany';

-- ✅ Gut: LIMIT in Subqueries
SELECT * 
FROM (
  SELECT * FROM large_table LIMIT 1000
) sub
WHERE condition;

-- ✅ Gut: Indexierte Spalten in WHERE/JOIN verwenden
```

#### CTEs statt Subqueries (für Lesbarkeit)
```sql
-- ✅ Gut: Mit CTE
WITH high_value_customers AS (
  SELECT customer_id
  FROM orders
  GROUP BY customer_id
  HAVING SUM(total) > 10000
),
recent_orders AS (
  SELECT *
  FROM orders
  WHERE order_date >= '2025-01-01'
)
SELECT *
FROM recent_orders ro
JOIN high_value_customers hvc 
  ON ro.customer_id = hvc.customer_id;

-- ❌ Kompliziert: Verschachtelte Subqueries
SELECT *
FROM (SELECT * FROM orders WHERE order_date >= '2025-01-01') ro
JOIN (SELECT customer_id FROM orders GROUP BY customer_id HAVING SUM(total) > 10000) hvc
  ON ro.customer_id = hvc.customer_id;
```

### ⚠️ Häufige Fehler vermeiden

```sql
-- ❌ SELECT * in Production
SELECT * FROM large_table;  -- Langsam, verschwendet Ressourcen

-- ❌ Fehlende WHERE in UPDATE/DELETE
DELETE FROM customers;  -- Löscht ALLES!

-- ❌ JOIN ohne ON (Cartesian Product)
SELECT * FROM table1, table2;  -- Explosiver Datensatz

-- ❌ Strings mit != NULL vergleichen
WHERE email != NULL  -- Funktioniert nicht!
-- ✅ Richtig:
WHERE email IS NOT NULL
```

---

## 📊 7. Visualisierung & Kommunikation

### ✅ Best Practices

#### Chart-Auswahl
```
Ziel                    → Diagrammtyp
────────────────────────────────────────
Vergleich               → Balkendiagramm
Zeitverlauf             → Liniendiagramm
Teil-vom-Ganzen         → Kreisdiagramm (max. 5-7 Segmente)
Verteilung              → Histogramm, Boxplot
Beziehung/Korrelation   → Scatterplot
Geografisch             → Karte, Heatmap
Hierarchie              → Treemap, Sunburst
```

#### Design-Prinzipien
```
✓ Weniger ist mehr
  - Max. 5-7 Farben pro Visualisierung
  - Fokus auf wichtigste Insights
  - Unnötige Dekorationen weglassen

✓ Accessibility
  - Farbblindheit berücksichtigen
  - Ausreichend Kontrast
  - Achsenbeschriftungen klar

✓ Ehrliche Darstellung
  - Y-Achse bei 0 starten (bei Mengen)
  - Keine manipulativen Skalierungen
  - Unsicherheit zeigen (Konfidenzintervalle)

✓ Kontext geben
  - Vergleichswerte (Benchmarks, Vorjahr)
  - Titel aussagekräftig
  - Quellen angeben
```

#### Storytelling mit Daten
```
Struktur:
1. Kontext setzen
   "Unser Umsatz ist um 15% gesunken"

2. Warum wichtig?
   "Das entspricht 2M€ Verlust und gefährdet Jahresziele"

3. Was ist passiert?
   "Analyse zeigt: 3 Hauptfaktoren..."
   [Visualisierung]

4. Was bedeutet das?
   "Wenn wir nichts tun, erwarten wir..."

5. Was empfehlen wir?
   "Unsere Top 3 Empfehlungen..."
```

### ⚠️ Häufige Fehler vermeiden

```
❌ 3D-Diagramme (verzerren Proportionen)
❌ Zu viele Daten in einem Chart
❌ Irreführende Achsen (nicht bei 0)
❌ Junk Charts (unnötige Dekorationen)
❌ Falsche Charttypen (Kreisdiagramm für Trends)
❌ Keine Beschriftungen/Legenden
```

---

## 📝 8. Dokumentation

### ✅ Best Practices

#### Was dokumentieren?
```
1. Projektdokumentation
   - Zielsetzung und Scope
   - Annahmen und Limitationen
   - Methodologie
   - Ergebnisse und Insights
   - Empfehlungen

2. Code-Dokumentation
   - Was macht der Code?
   - Warum diese Methode?
   - Input/Output
   - Dependencies
   - Beispiele

3. Daten-Dokumentation
   - Datenquellen
   - Schema (Tabellen, Spalten)
   - Bereinigungsschritte
   - Transformationen
   - Bekannte Issues
```

#### README-Template
```markdown
# Projekt: Kundenabwanderungsanalyse Q3 2025

## Zielsetzung
Identifiziere Hauptgründe für 25% Churn-Anstieg

## Daten
- Quelle: CRM-System (Export 01.10.2025)
- Zeitraum: Jan 2024 - Sep 2025
- Umfang: 50.000 Kunden, 150.000 Transaktionen

## Methodik
1. Datenbereinigung (siehe cleaning_script.sql)
2. RFM-Segmentierung
3. Logistische Regression
4. Feature Importance Analyse

## Wichtigste Erkenntnisse
1. Kunden mit Support-Tickets > 3 churnen 5x häufiger
2. Preiserhöhung im März korreliert mit Churn-Spike
3. Onboarding-Qualität ist #1 Prädiktor

## Empfehlungen
1. Proaktive Support-Eskalation bei 3+ Tickets
2. Preiserhöhungs-Kommunikation verbessern
3. Onboarding-Prozess überarbeiten

## Files
- data/: Rohdaten und bereinigt
- scripts/: SQL und Python Scripts
- results/: Outputs und Visualisierungen
- report.pdf: Executive Summary
```

#### Code-Kommentare
```sql
-- ✅ Gut: Erklärt WARUM, nicht WAS
-- Verwende LEFT JOIN um auch Kunden ohne Bestellungen zu inkludieren
-- Business-Anforderung: Alle Kunden sollen in Report erscheinen
SELECT c.*, COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

-- ❌ Schlecht: Wiederholt nur den Code
-- Left join customers und orders
SELECT c.*, COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;
```

---

## 🔄 9. Reproduzierbarkeit & Versionierung

### ✅ Best Practices

#### Git für Versionskontrolle
```bash
# Struktur
project/
├── data/
│   ├── raw/              # Originaldaten (nicht versioniert)
│   └── processed/        # Bereinigt (nicht versioniert)
├── scripts/
│   ├── 01_cleaning.sql
│   ├── 02_analysis.sql
│   └── 03_visualization.py
├── results/
│   └── report.pdf
├── README.md
└── requirements.txt      # Dependencies
```

#### Reproduzierbare Analysen
```python
# ✅ Gut: Seed für Zufallsgenerierung
import numpy as np
np.random.seed(42)

# ✅ Gut: Dependencies dokumentieren
# requirements.txt
pandas==2.0.0
numpy==1.24.0
scikit-learn==1.3.0

# ✅ Gut: Relative Pfade
import os
data_path = os.path.join(os.getcwd(), 'data', 'raw', 'customers.csv')
```

---

## 🚀 10. Continuous Improvement

### ✅ Best Practices

#### Nach jedem Projekt
```
✓ Was lief gut?
✓ Was könnte verbessert werden?
✓ Welche Tools/Methoden waren effektiv?
✓ Was habe ich gelernt?
✓ Feedback von Stakeholdern einholen
```

#### Weiterbildung
```
✓ Neue Tools/Techniken ausprobieren
✓ Best Practices anderer lernen
✓ Code Reviews durchführen/erhalten
✓ Community teilnehmen (Kaggle, Reddit, etc.)
✓ Eigene Projekte für Portfolio
```

---

## 📚 Checkliste: Projekt-Review

Bevor Projekt als "abgeschlossen" markiert wird:

**Datenqualität**
- [ ] Alle Bereinigungsschritte dokumentiert
- [ ] Datenquellen validiert
- [ ] Edge Cases geprüft
- [ ] Nullwerte behandelt

**Analyse**
- [ ] Annahmen explizit genannt
- [ ] Statistische Tests korrekt angewendet
- [ ] Sensitivitätsanalyse durchgeführt
- [ ] Alternative Erklärungen geprüft

**Visualisierung**
- [ ] Charttypen passend gewählt
- [ ] Achsen korrekt beschriftet
- [ ] Legenden verständlich
- [ ] Farben accessibility-freundlich

**Kommunikation**
- [ ] Executive Summary vorhanden
- [ ] Kernbotschaft klar
- [ ] Empfehlungen actionable
- [ ] Limitationen transparent

**Dokumentation**
- [ ] README vollständig
- [ ] Code kommentiert
- [ ] Reproduzierbarkeit gegeben
- [ ] Dependencies dokumentiert

**Stakeholder**
- [ ] Erwartungen erfüllt
- [ ] Feedback eingeholt
- [ ] Follow-up-Fragen beantwortet
- [ ] Nächste Schritte definiert

---

*Aktualisiert: Oktober 2025*