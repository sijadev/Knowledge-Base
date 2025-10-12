---
autor: Simon Janke
title: Google Sheets / Excel Cheat Sheet
type: Ressource
date: 2025-10-12
tags:
  - spreadsheets
  - excel
  - google-sheets
  - formeln
  - cheat-sheet
---

# 📊 Google Sheets / Excel Cheat Sheet

---

## 🎯 Grundlegende Operationen

### Mathematische Operatoren
```
=A1 + B1    Addition
=A1 - B1    Subtraktion
=A1 * B1    Multiplikation
=A1 / B1    Division
=A1 ^ 2     Potenz (Quadrat)
=A1 % 10    Modulo (Rest)
```

### Zellreferenzen
```
A1          Relative Referenz (ändert sich beim Kopieren)
$A$1        Absolute Referenz (bleibt fix)
$A1         Spalte fix, Zeile variabel
A$1         Zeile fix, Spalte variabel
```

---

## 📊 Aggregationsfunktionen

### SUM (Summe)
```excel
=SUM(A1:A10)                    // Summe von A1 bis A10
=SUM(A1:A10, C1:C10)           // Mehrere Bereiche
=SUMIF(A1:A10, ">100")         // Summe wenn Bedingung erfüllt
=SUMIF(B1:B10, "Deutschland", C1:C10)  // Summe wenn Land = Deutschland
=SUMIFS(C1:C10, B1:B10, "Deutschland", D1:D10, ">2025-01-01")  // Mehrere Bedingungen
```

### AVERAGE (Durchschnitt)
```excel
=AVERAGE(A1:A10)
=AVERAGEIF(A1:A10, ">100")
=AVERAGEIFS(C1:C10, B1:B10, "Deutschland", D1:D10, ">100")
```

### COUNT (Zählen)
```excel
=COUNT(A1:A10)                  // Zählt nur Zahlen
=COUNTA(A1:A10)                 // Zählt alle nicht-leeren Zellen
=COUNTBLANK(A1:A10)             // Zählt leere Zellen
=COUNTIF(A1:A10, ">100")        // Zählt wenn Bedingung erfüllt
=COUNTIFS(B1:B10, "Deutschland", C1:C10, ">100")  // Mehrere Bedingungen
```

### MIN / MAX
```excel
=MIN(A1:A10)                    // Kleinster Wert
=MAX(A1:A10)                    // Größter Wert
=MINIFS(C1:C10, B1:B10, "Deutschland")  // Min mit Bedingung
=MAXIFS(C1:C10, B1:B10, "Deutschland")  // Max mit Bedingung
```

---

## 🔍 Lookup-Funktionen

### VLOOKUP (Vertikale Suche)
```excel
=VLOOKUP(suchkriterium, bereich, spaltenindex, [ungefähr])

Beispiel:
=VLOOKUP(A2, Products!A:D, 3, FALSE)
// Sucht A2 in Spalte A der Tabelle "Products"
// Gibt Wert aus Spalte 3 zurück
// FALSE = exakte Übereinstimmung
```

**Praktisches Beispiel:**
```
Produkt-ID in A2: "P123"
Products-Tabelle:
  A         B           C         D
  ID        Name        Preis     Kategorie
  P123      Laptop      899       Electronics
  P124      Mouse       29        Accessories

=VLOOKUP(A2, Products!A:D, 3, FALSE)  → gibt 899 zurück
```

### HLOOKUP (Horizontale Suche)
```excel
=HLOOKUP(suchkriterium, bereich, zeilenindex, [ungefähr])

// Wie VLOOKUP, aber sucht in Zeilen statt Spalten
```

### XLOOKUP (Modern, nur neuere Versionen)
```excel
=XLOOKUP(suchkriterium, sucharray, rückgabearray, [wenn_nicht_gefunden])

Beispiel:
=XLOOKUP(A2, Products!A:A, Products!C:C, "Nicht gefunden")
// Flexibler als VLOOKUP, keine Spaltenindex-Nummer nötig
```

### INDEX + MATCH (Fortgeschritten, sehr flexibel)
```excel
=INDEX(rückgabebereich, MATCH(suchkriterium, suchbereich, 0))

Beispiel:
=INDEX(Products!C:C, MATCH(A2, Products!A:A, 0))
// Gleiche Funktionalität wie VLOOKUP, aber flexibler
// Kann links suchen, VLOOKUP nur rechts
```

---

## 📝 Text-Funktionen

### Kombinieren
```excel
=CONCATENATE(A1, " ", B1)       // Alt
=CONCAT(A1, " ", B1)            // Neu
=A1 & " " & B1                  // Operator-Methode

// Textjoin (mit Trennzeichen)
=TEXTJOIN(", ", TRUE, A1:A10)   // Verknüpft mit Komma, ignoriert Leerzeichen
```

### Extrahieren
```excel
=LEFT(A1, 3)                    // Erste 3 Zeichen
=RIGHT(A1, 3)                   // Letzte 3 Zeichen
=MID(A1, 2, 5)                  // Ab Position 2, 5 Zeichen

Beispiel:
A1 = "Hello World"
=LEFT(A1, 5)      → "Hello"
=RIGHT(A1, 5)     → "World"
=MID(A1, 7, 5)    → "World"
```

### Groß-/Kleinschreibung
```excel
=UPPER(A1)                      // ALLES GROSS
=LOWER(A1)                      // alles klein
=PROPER(A1)                     // Jedes Wort Groß

Beispiel:
A1 = "hello world"
=PROPER(A1)  → "Hello World"
```

### Trimmen & Bereinigen
```excel
=TRIM(A1)                       // Entfernt überflüssige Leerzeichen
=CLEAN(A1)                      // Entfernt nicht-druckbare Zeichen
=SUBSTITUTE(A1, "alt", "neu")   // Ersetzt Text

Beispiel:
A1 = "  Hello   World  "
=TRIM(A1)  → "Hello World"
```

### Suchen & Finden
```excel
=FIND("text", A1)               // Case-sensitive
=SEARCH("text", A1)             // Nicht case-sensitive
=LEN(A1)                        // Länge des Textes

Beispiel:
A1 = "Hello World"
=FIND("World", A1)  → 7 (Position)
=LEN(A1)            → 11
```

---

## 📅 Datumsfunktionen

### Aktuelles Datum/Zeit
```excel
=TODAY()                        // Aktuelles Datum
=NOW()                          // Aktuelles Datum + Uhrzeit
```

### Datum erstellen
```excel
=DATE(2025, 10, 12)            // Jahr, Monat, Tag
=DATEVALUE("12.10.2025")       // Text zu Datum konvertieren
```

### Datum extrahieren
```excel
=YEAR(A1)                       // Jahr extrahieren
=MONTH(A1)                      // Monat (1-12)
=DAY(A1)                        // Tag (1-31)
=WEEKDAY(A1)                    // Wochentag (1=Sonntag)

Beispiel:
A1 = 12.10.2025
=YEAR(A1)       → 2025
=MONTH(A1)      → 10
=WEEKDAY(A1)    → 1 (Sonntag)
```

### Datumsdifferenz
```excel
=DATEDIF(startdatum, enddatum, einheit)

Einheiten:
"D" = Tage
"M" = Monate
"Y" = Jahre
"MD" = Tage (Monate/Jahre ignoriert)
"YM" = Monate (Jahre ignoriert)

Beispiel:
=DATEDIF("01.01.2025", "31.12.2025", "D")  → 364 Tage
=DATEDIF("01.01.2020", "31.12.2025", "Y")  → 5 Jahre
```

### Datums-Arithmetik
```excel
=A1 + 7                         // 7 Tage hinzufügen
=EDATE(A1, 3)                   // 3 Monate hinzufügen
=EOMONTH(A1, 0)                 // Letzter Tag des Monats
=EOMONTH(A1, 1)                 // Letzter Tag des nächsten Monats

Beispiel:
A1 = 12.10.2025
=EDATE(A1, 3)      → 12.01.2026
=EOMONTH(A1, 0)    → 31.10.2025
```

---

## 🔀 Logische Funktionen

### IF (Wenn-Dann)
```excel
=IF(bedingung, wert_wenn_wahr, wert_wenn_falsch)

Beispiel:
=IF(A1 > 100, "Hoch", "Niedrig")
=IF(B1 = "Deutschland", A1 * 1.19, A1)  // MwSt. nur für DE
```

### Verschachtelte IFs
```excel
=IF(A1 >= 90, "A", 
    IF(A1 >= 80, "B", 
        IF(A1 >= 70, "C", 
            IF(A1 >= 60, "D", "F"))))
```

### IFS (Moderner, nur neuere Versionen)
```excel
=IFS(
  A1 >= 90, "A",
  A1 >= 80, "B",
  A1 >= 70, "C",
  A1 >= 60, "D",
  TRUE, "F"
)
```

### AND / OR / NOT
```excel
=AND(A1 > 100, B1 = "Deutschland")      // Beide müssen wahr sein
=OR(A1 > 100, B1 = "Deutschland")       // Mindestens eine muss wahr sein
=NOT(A1 > 100)                           // Kehrt Ergebnis um

Beispiel:
=IF(AND(A1 > 100, B1 = "VIP"), "Discount", "Regular Price")
```

### IFERROR (Fehlerbehandlung)
```excel
=IFERROR(formel, wert_bei_fehler)

Beispiel:
=IFERROR(A1/B1, 0)                      // Wenn Fehler, dann 0
=IFERROR(VLOOKUP(A1, B:C, 2, FALSE), "Nicht gefunden")
```

---

## 📊 Pivot-Tabellen-Funktionen

### GETPIVOTDATA
```excel
=GETPIVOTDATA(datenfeld, pivot_tabelle, [feld1, wert1, ...])

Beispiel:
=GETPIVOTDATA("Summe von Umsatz", $A$1, "Land", "Deutschland", "Jahr", 2025)
```

---

## 🎨 Bedingte Formatierung (Formeln)

### Zeile basierend auf Wert färben
```excel
=$B1 > 1000                     // Färbt ganze Zeile wenn B > 1000
```

### Duplikate markieren
```excel
=COUNTIF($A$1:$A$100, A1) > 1  // Markiert Duplikate in Spalte A
```

### Alternierend färben
```excel
=MOD(ROW(), 2) = 0             // Färbt jede zweite Zeile
```

---

## 📈 Statistische Funktionen

### Grundlegende Statistik
```excel
=MEDIAN(A1:A10)                 // Median (mittlerer Wert)
=MODE(A1:A10)                   // Häufigster Wert
=STDEV(A1:A10)                  // Standardabweichung (Stichprobe)
=STDEVP(A1:A10)                 // Standardabweichung (Population)
=VAR(A1:A10)                    // Varianz
```

### Perzentile & Quartile
```excel
=PERCENTILE(A1:A100, 0.95)      // 95. Perzentil
=QUARTILE(A1:A100, 1)           // 1. Quartil (25%)
```

### Ranking
```excel
=RANK(wert, bereich, [reihenfolge])

Beispiel:
=RANK(A1, $A$1:$A$10, 0)       // Rang (0 = absteigend, 1 = aufsteigend)
```

---

## 🔢 Erweiterte Formeln

### ARRAYFORMULA (Google Sheets)
```excel
=ARRAYFORMULA(A1:A10 * B1:B10)  // Multipliziert ganze Spalten

// Mit IF:
=ARRAYFORMULA(IF(A2:A100 > 100, "Hoch", "Niedrig"))
```

### QUERY (Google Sheets - SQL-ähnlich)
```excel
=QUERY(A1:D100, "SELECT A, SUM(C) WHERE B = 'Deutschland' GROUP BY A")

Syntax wie SQL:
SELECT, WHERE, GROUP BY, ORDER BY, LIMIT
```

### FILTER (Google Sheets & neue Excel-Versionen)
```excel
=FILTER(bereich, bedingung1, [bedingung2, ...])

Beispiel:
=FILTER(A2:D100, B2:B100 = "Deutschland", C2:C100 > 1000)
// Filtert Zeilen wo Land = Deutschland UND Umsatz > 1000
```

### UNIQUE (Einzigartige Werte)
```excel
=UNIQUE(A2:A100)                // Alle einzigartigen Werte

// Mit SORT kombinieren:
=SORT(UNIQUE(A2:A100))
```

### SORT (Sortieren)
```excel
=SORT(bereich, [sort_spalte], [aufsteigend])

Beispiel:
=SORT(A2:D100, 3, FALSE)       // Sortiert nach Spalte 3, absteigend
```

---

## 🎯 Häufige Use Cases

### 1. Bereinigung: Leerzeichen und Formatierung
```excel
=TRIM(CLEAN(UPPER(A1)))         // Bereinigt + Großbuchstaben
```

### 2. Email-Extraktion aus Text
```excel
=MID(A1, FIND("@", A1) - 10, 30)
```

### 3. Voller Name in Vor- und Nachname
```excel
Vorname:  =LEFT(A1, FIND(" ", A1) - 1)
Nachname: =RIGHT(A1, LEN(A1) - FIND(" ", A1))
```

### 4. Alternativer Text bei Fehler
```excel
=IFERROR(VLOOKUP(A1, B:C, 2, FALSE), "Nicht gefunden")
```

### 5. Dynamischer Bereich
```excel
=OFFSET(A1, 0, 0, COUNTA(A:A), 1)  // Wächst mit Daten
```

### 6. N-te Wert finden
```excel
=INDEX(A:A, SMALL(IF(B:B = "Deutschland", ROW(B:B)), 1))
// Erster "Deutschland"-Eintrag
```

### 7. Summe der Top 5 Werte
```excel
=SUMPRODUCT(LARGE(A1:A100, ROW(1:5)))
```

### 8. Verkettung mit Bedingung
```excel
=TEXTJOIN(", ", TRUE, IF(B1:B10 = "Aktiv", A1:A10, ""))
// Nur aktive Namen verbinden
```

---

## ⚠️ Häufige Fehler & Lösungen

### #DIV/0! (Division durch 0)
```excel
// Problem:
=A1/B1  // B1 ist 0

// Lösung:
=IFERROR(A1/B1, 0)
=IF(B1 = 0, 0, A1/B1)
```

### #N/A (Wert nicht gefunden)
```excel
// Problem:
=VLOOKUP(A1, B:C, 2, FALSE)  // A1 nicht in B gefunden

// Lösung:
=IFERROR(VLOOKUP(A1, B:C, 2, FALSE), "Nicht vorhanden")
```

### #REF! (Ungültige Referenz)
```excel
// Problem: Spalte/Zeile wurde gelöscht

// Lösung: Formel neu erstellen mit korrekten Referenzen
```

### #VALUE! (Falscher Datentyp)
```excel
// Problem: Text in mathematischer Operation

// Lösung:
=VALUE(A1) + B1  // Text zu Zahl konvertieren
```

---

## 💡 Best Practices

### 1. Benannte Bereiche verwenden
```excel
// Statt: =SUM(A1:A100)
// Besser: =SUM(Umsätze)
```

### 2. Absolute Referenzen für Konstanten
```excel
=A1 * $B$1  // MwSt.-Satz in B1 bleibt fix beim Kopieren
```

### 3. Formeln dokumentieren
```excel
// Kommentar in benachbarte Zelle:
"Berechnet Nettopreis mit 19% MwSt."
```

### 4. IFERROR für Robustheit
```excel
// Immer Fehler abfangen in Production-Sheets
=IFERROR(deine_formel, fallback_wert)
```

### 5. Datenvalidierung nutzen
```
Daten → Datenvalidierung → Liste/Bereich
→ Verhindert Eingabefehler
```

---

## 🚀 Power-User Shortcuts

### Allgemein
```
Strg + ;        Aktuelles Datum einfügen
Strg + :        Aktuelle Uhrzeit einfügen
Strg + '        Formel von Zelle oben kopieren
F4              Zwischen relativen/absoluten Referenzen wechseln
```

### Navigation
```
Strg + Pfeiltasten      Zum Ende des Datenbereichs
Strg + Home             Zu A1
Strg + End              Zur letzten Zelle mit Daten
```

### Auswahl
```
Strg + Shift + Pfeil    Bereich bis zum Ende auswählen
Strg + A                Alles auswählen
Shift + Leertaste       Ganze Zeile auswählen
Strg + Leertaste        Ganze Spalte auswählen
```

---

## 📚 Weiterführende Ressourcen

- [Google Sheets Functions List](https://support.google.com/docs/table/25273)
- [Excel Functions Reference](https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188)
- [Exceljet - Formulas & Functions](https://exceljet.net/formulas)

---

*Aktualisiert: Oktober 2025*