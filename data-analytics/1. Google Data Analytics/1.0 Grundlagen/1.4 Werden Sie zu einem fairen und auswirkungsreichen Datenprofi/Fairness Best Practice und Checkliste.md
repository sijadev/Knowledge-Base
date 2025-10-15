---
autor: Simon Janke
title: Fairness Checkliste & Best Practice
type: Google Data Analytics Kurs
date: 2025-10-14
tags:
  - "#fairness-checkliste"
  - "#fairness"
  - "#fairness-best-practice"
links:
  - "[[Grundlagen]]"
---

## 🔍 Praktische Fairness-Checkliste:

**Vor der Datenerhebung:**

- [ ] Ist meine Methode für alle Zielgruppen gleich zugänglich?
- [ ]  Erfasse ich zu verschiedenen Zeiten/an verschiedenen Orten?
- [ ]  Habe ich bewusst diverse Quellen gewählt?

**Nach der Datenerhebung:**

- [ ]  Spiegelt mein Datensatz die bekannte Verteilung der Population?
- [ ]  Gibt es auffällige Über-/Unterrepräsentationen?
- [ ]  Habe ich ausreichend Daten von Minderheitengruppen?

**Während der Analyse:**

- [ ]  Teste ich meine Ergebnisse für verschiedene Subgruppen?
- [ ]  Funktioniert mein Modell für alle Gruppen gleich gut?
- [ ]  Kommuniziere ich Einschränkungen transparent?

---

## ✅ Best Practice Ansatz (5-Schritte-Methode):

### 1. **Definiere deine Ziel-Population klar**

- Über wen möchte ich Aussagen treffen?
- Wer sollte in meinen Daten vertreten sein?

### 2. **Identifiziere relevante Dimensionen**

Überlege, welche Merkmale für deine Analyse wichtig sind:

- Demografie (Alter, Geschlecht, Einkommen, Bildung)
- Geografie (Stadt/Land, Region)
- Verhalten (aktive/inaktive Nutzer)
- Zeit (verschiedene Zeiträume)

### 3. **Stratified Sampling nutzen**

Stelle sicher, dass wichtige Untergruppen proportional vertreten sind. **Beispiel:** Wenn 30% deiner Kunden weiblich sind, sollten auch ~30% deiner Daten von Frauen stammen.

### 4. **Mehrere Datenquellen kombinieren**

Eine einzelne Quelle hat oft blinde Flecken:

- Online + Offline Kanäle
- Verschiedene geografische Regionen
- Unterschiedliche Erfassungsmethoden

### 5. **Dokumentiere deine Limitationen**

Ehrlichkeit ist wichtig! Schreibe auf:

- Welche Gruppen fehlen oder sind unterrepräsentiert?
- Warum fehlen sie?
- Wie könnte das die Ergebnisse beeinflussen?


## 💡 Konkrete Techniken:

**Minimum Sample Size pro Gruppe:**

- Faustregel: Mindestens 30-50 Datenpunkte pro relevanter Subgruppe
- Bei kleineren Gruppen: Oversampling erwägen (mehr Daten von unterrepräsentierten Gruppen sammeln)

**Bias-Audits durchführen:**

- Vergleiche deine Datenverteilung mit offiziellen Statistiken (z.B. Zensus-Daten)
- Berechne Repräsentativitäts-Metriken

**Diversität im Team:**

- Menschen mit verschiedenen Hintergründen erkennen unterschiedliche Bias-Quellen

## ⚠️ Warnsignale für unfaire Datensätze:

- Convenience Sampling (einfach die Daten nehmen, die gerade verfügbar sind)
- Nur freiwillige Teilnahme ohne Strategie
- Sehr homogene Datenquelle
- Historische Daten ohne kritische Prüfung (alte Daten können alte Vorurteile enthalten)
- Fehlende Dokumentation über Erhebungsmethode

## 📊 Praxis-Beispiel:

**Schlecht:** Kundenzufriedenheits-Umfrage nur per E-Mail → nur technikaffine Kunden antworten

**Besser:** E-Mail + Telefon + In-Store → verschiedene Kundentypen erreicht

**Am besten:** Stratified Sampling nach Kundentyp (neu/alt, online/offline) + mehrere Kanäle + bewusste Nachfass-Aktionen bei schwer erreichbaren Gruppen

---

**Wichtigste Erkenntnis:** Perfekte Fairness ist oft unmöglich, aber **bewusster Umgang** mit Limitationen und **transparente Kommunikation** sind entscheidend! 🎯

---