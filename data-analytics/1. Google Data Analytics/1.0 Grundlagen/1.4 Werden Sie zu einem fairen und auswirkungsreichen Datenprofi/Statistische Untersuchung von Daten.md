---
autor: Simon Janke
title: Statistische Untersuchung von Daten
type: Google Data Analytics Kurs
date: 2025-10-14
tags:
  - "#statistik"
  - "#bias"
links:
  - "[[Grundlagen]]"
---
---
## ✅ Warum IMMER statistische Untersuchungen?

### 1. **Du musst deine Daten kennen, bevor du sie analysierst**

Ohne statistische Untersuchung weißt du nicht:

- Ob deine Daten sinnvoll sind
- Ob Fehler oder Ausreißer existieren
- Ob deine geplante Analyse überhaupt funktionieren kann

### 2. **Bias-Erkennung** (dein aktuelles Thema!)

Statistische Checks zeigen dir:

- Unterrepräsentierte Gruppen
- Verzerrungen in der Verteilung
- Fehlende Werte (oft nicht zufällig!)

### 3. **Vermeidung von Fehlinterpretationen**

Ohne Stats könntest du:

- Falsche Schlüsse ziehen
- Korrelation mit Kausalität verwechseln
- Wichtige Muster übersehen

## 📊 Standard-Prozess: Exploratory Data Analysis (EDA)

Das hast du sicher in deiner Google-Schulung gelernt! EDA ist der **erste Schritt** nach dem Daten-Import:

### **Phase 1: Überblick verschaffen**

```
- Anzahl Zeilen/Spalten
- Datentypen prüfen
- Erste Zeilen anschauen (head/tail)
- Struktur verstehen
```

### **Phase 2: Deskriptive Statistik**

**Für numerische Variablen:**

- Mean (Durchschnitt)
- Median (Mittelwert)
- Standardabweichung
- Min/Max
- Quartile (25%, 50%, 75%)

**Für kategorische Variablen:**

- Häufigkeitsverteilungen
- Anzahl eindeutiger Werte
- Häufigste Kategorien

### **Phase 3: Datenqualität prüfen**

- Fehlende Werte (NULL, NA) → Wie viele? Wo?
- Duplikate identifizieren
- Ausreißer erkennen
- Inkonsistenzen finden

### **Phase 4: Verteilungen verstehen**

- Histogramme erstellen
- Boxplots für Ausreißer
- Normalverteilung prüfen (wenn relevant)

### **Phase 5: Beziehungen erkunden**

- Korrelationen zwischen Variablen
- Crosstabs für kategorische Daten
- Scatter Plots für Zusammenhänge

## 🎯 Konkrete Tools/Befehle:

**In Python (Pandas):**

python

```python
# Schnell-Übersicht
df.info()              # Struktur, Datentypen
df.describe()          # Deskriptive Statistik
df.head()              # Erste Zeilen
df.isnull().sum()      # Fehlende Werte
df.duplicated().sum()  # Duplikate

# Verteilungen
df['spalte'].value_counts()  # Häufigkeiten
df['spalte'].hist()          # Histogramm

# Beziehungen
df.corr()  # Korrelationsmatrix
```

**In SQL:**


```sql
-- Basis-Stats
SELECT 
    COUNT(*) as total_rows,
    COUNT(DISTINCT customer_id) as unique_customers,
    AVG(sales) as avg_sales,
    MIN(sales) as min_sales,
    MAX(sales) as max_sales
FROM sales_data;

-- Fehlende Werte
SELECT 
    SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) as missing_emails
FROM customers;
```

**In Excel/Sheets:**

- Pivot Tables
- AVERAGE(), MEDIAN(), STDEV()
- COUNTIF() für Häufigkeiten
- Conditional Formatting für Ausreißer

## ⚡ Wann wie viel?

### **Minimum (IMMER):**

- Zeilen/Spalten zählen
- Datentypen prüfen
- Fehlende Werte checken
- Mean/Median für wichtige Variablen
- Duplikate suchen

### **Standard (normalerweise):**

- Vollständige deskriptive Statistik
- Verteilungen visualisieren
- Korrelationen prüfen
- Ausreißer identifizieren

### **Intensiv (bei komplexen Projekten):**

- Detaillierte Subgruppen-Analysen
- Multiple Visualisierungen
- Statistische Tests (t-Tests, Chi-Quadrat etc.)
- Bias-Audits

## 🚨 Was passiert OHNE statistische Untersuchung?

**Echte Horror-Beispiele:**

❌ **Beispiel 1: Fehlende Werte** Ohne Check: "Durchschnittliches Alter: 45 Jahre" Mit Check: "20% fehlende Werte bei Alter - könnten systematisch jüngere User sein!"

❌ **Beispiel 2: Ausreißer** Ohne Check: "Durchschnittlicher Umsatz: 500.000€" Mit Check: "Ein Mega-Deal von 50 Mio€ verzerrt alles - Median ist 5.000€!"

❌ **Beispiel 3: Skalierung** Ohne Check: Alter in Jahren (18-80), Einkommen in Euro (20.000-200.000) Problem: ML-Modelle funktionieren schlecht, weil Skalen unterschiedlich!

## 📋 Best Practice Workflow:

```
1. Daten importieren
   ↓
2. ⭐ STATISTISCHE UNTERSUCHUNG (EDA) ⭐
   ↓
3. Datenbereinigung (basierend auf Findings)
   ↓
4. Nochmal Stats (sind Daten jetzt OK?)
   ↓
5. Eigentliche Analyse
   ↓
6. Ergebnisse interpretieren
```

## 💡 Im Kontext deiner Bias-Frage:

Statistische Untersuchungen helfen dir konkret bei Fairness:

**Checkst du z.B.:**

- Geschlechterverteilung: 80% männlich, 20% weiblich → Bias-Warnung!
- Altersverteilung: Keine Personen über 60 → Bias-Warnung!
- Geografische Verteilung: 95% aus Großstädten → Bias-Warnung!

## ✅ Zusammenfassung:

**Statistische Datenuntersuchungen sind:**

1. ✓ Obligatorisch, nicht optional
2. ✓ Der erste Schritt nach Daten-Import
3. ✓ Essentiell für Bias-Erkennung
4. ✓ Basis für alle weiteren Entscheidungen
5. ✓ Teil jeder Data Analytics Best Practice

**Faustregel:** Mindestens 20-30% deiner Analyse-Zeit sollte in EDA fließen!

---

