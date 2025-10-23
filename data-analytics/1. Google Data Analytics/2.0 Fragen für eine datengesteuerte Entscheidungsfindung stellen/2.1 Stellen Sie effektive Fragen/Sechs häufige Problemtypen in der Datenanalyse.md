---
autor: Simon Janke
title: Häufige Problemtypen in der Datenanalyse
type: Google Data Analytics Kurs
date: 2025-10-21
tags:
  - "#problemtypen"
  - Fragephase
  - "#workflow"
links:
  - "[[Fragen für datengesteuerte Entscheidungsfindung]]"
---
---

## Problemtypen anhand den **Daten** identifizieren

**1. Vorhersagen treffen:**
- Bei diesem Problemtyp werden Daten verwendet, um eine fundierte Entscheidung darüber zu treffen, wie die Dinge in Zukunft aussehen könnten.
- bezieht sich auf prädiktive Modelle – etwa die Vorhersage von Verkaufszahlen, Kundenabwanderung oder Aktienkursen basierend auf historischen Daten.

**2. Dinge kategorisieren:** 
- Dies bedeutet, dass Informationen auf der Grundlage gemeinsamer Merkmale verschiedenen Gruppen oder Clustern zugewiesen werden.
- bedeutet Klassifikation oder Segmentierung – zum Beispiel E-Mails als Spam oder legitim einordnen, Kunden in Segmente unterteilen oder Produkte automatisch Kategorien zuweisen.

**3. Etwas Ungewöhnliches entdecken:** 
- Bei diesem Problemtyp identifizieren Datenanalysten Daten , die von der Norm abweichen.
- ist die Anomalieerkennung – Betrugsversuche in Transaktionsdaten identifizieren, fehlerhafte Messwerte aufdecken oder unerwartete Abweichungen in Prozessen erkennen.

**4. Themen identifizieren:** 
- Bei der Identifizierung von Themen geht die Kategorisierung noch einen Schritt weiter, indem Informationen zu umfassenderen Konzepten zusammengefasst werden.
- bedeutet, Struktur in ungeordneten Daten zu finden – etwa automatisch Themen in Kundenfeedback oder News-Artikeln erkennen (Topic Modeling).

**5. Zusammenhänge entdecken:** 
- Der Problemtyp der Erkennung von Zusammenhängen ermöglicht es Datenanalysten nun, ähnliche Herausforderungen zu finden, mit denen verschiedene Unternehmen konfrontiert sind, und dann Daten und Erkenntnisse zu kombinieren, um sie zu lösen.
- fokussiert auf Korrelationen und Abhängigkeiten – welche Faktoren beeinflussen sich gegenseitig? Was hängt mit was zusammen?

**6. Muster finden:** 
- Datenanalysten verwenden Daten, um Muster zu finden, indem sie historische Daten verwenden, um zu verstehen, was in der Vergangenheit passiert ist und daher wahrscheinlich wieder passieren wird.
- ist die Suche nach wiederkehrenden Strukturen – Kaufmuster von Kunden, zeitliche Trends oder wiederkehrende Abläufe in Prozessdaten.


```Zitat
Frage: Man erkennt erst durch passende Vorgehensweise die Problemtypen und kann in der Fragephase nur eine Hypothese erstellen ?
```

### KI Antwort: 

Genau, das ist ein sehr wichtiger und realistischer Punkt! Du beschreibst da einen iterativen Prozess, der in der Praxis oft so abläuft:

**In der Fragephase** startet man tatsächlich oft mit Unsicherheit. Man hat ein vages Geschäftsproblem oder eine allgemeine Frage, aber die genaue Natur des Analyseproblems ist noch nicht klar. Man formuliert Hypothesen oder erste Vermutungen: "Vielleicht hängt das mit Faktor X zusammen" oder "Möglicherweise gibt es hier ein Muster."

**Durch explorative Analysen und die Wahl der Vorgehensweise** werden die Problemtypen erst konkret. Wenn man beispielsweise beginnt, Daten zu visualisieren oder erste statistische Tests durchzuführen, wird deutlicher, ob man es eher mit Kategorisierung, Anomalieerkennung oder Mustererkennung zu tun hat.

**Das Erkennen des eigentlichen Problemtyps** ist also nicht am Anfang gegeben, sondern entwickelt sich. Man könnte mit der Hypothese starten "Wir möchten Kunden besser verstehen" und durch die Analyse erst feststellen, dass es letztlich um Segmentierung (Kategorisierung) oder um das Identifizieren von Abweichlergruppen (Anomalieerkennung) geht.

Das heißt, die Problemformulierung ist selbst Teil des Analyseprozesses – man verfeinert sie iterativ, je mehr man über die Daten lernt. Das ist völlig normal und zeigt, dass Datenanalyse ein explorativer Prozess ist, kein linearer.

### Workflow:

Das Modul lehrt einen Workflow wie diesen:

1. **Problem verstehen** – Was ist die eigentliche Geschäftsfrage? Was soll erreicht werden?
2. **Hypothesen formulieren** – Erste Vermutungen aufstellen, wie das Problem gelöst werden könnte
3. **Passende Problemtypen identifizieren** – Durch Analyse und Vorgehensweise wird klar: "Ah, das ist eigentlich ein Kategorisierungsproblem" oder "Das erfordert Anomalieerkennung"
4. **Geeignete Techniken anwenden** – Je nach erkanntem Problemtyp werden unterschiedliche Methoden, Tools und Analysetechniken gewählt
5. **Erkenntnisse gewinnen und handeln** – Die Ergebnisse in konkrete Maßnahmen umsetzen

Die sechs Problemtypen sind dann quasi die "Werkzeuge" in deinem Werkzeugkasten – du lernst, welches Werkzeug für welche Situation passt und wie du es einsetzt.

Das erklärt auch, warum die Vorgehensweise so wichtig ist: Sie offenbart erst, welcher Problemtyp wirklich vorliegt und führt dich zur richtigen Lösung.

## Real World Beispiele:

### **Vorhersagen machen**

Ein Unternehmen, das wissen möchte, welche Werbemethode am besten geeignet ist, um neue Kunden zu gewinnen, ist ein Beispiel für ein Problem, bei dem Analysten Vorhersagen machen müssen. Analysten, die über Daten zum Standort, zur Art der Medien und zur Anzahl der durch frühere Werbemaßnahmen gewonnenen Neukunden verfügen, können zwar keine Garantie für zukünftige Ergebnisse geben, aber sie können dabei helfen, die beste Platzierung der Werbung vorherzusagen, um die Zielgruppe zu erreichen.

### **Dinge kategorisieren**

Ein Beispiel für ein Problem, bei dem Analysten Dinge kategorisieren müssen, ist das Ziel eines Unternehmens, die Kundenzufriedenheit zu verbessern. Analysten könnten Kundendienstanrufe auf der Grundlage bestimmter Schlüsselwörter oder Punktzahlen klassifizieren. Dies könnte dabei helfen, die leistungsstärksten Kundendienstmitarbeiter zu identifizieren oder bestimmte Maßnahmen mit höheren Kundenzufriedenheitswerten zu korrelieren.

### **Erkennen von etwas Ungewöhnlichem**

Ein Unternehmen, das intelligente Uhren verkauft, die den Menschen helfen, ihre Gesundheit zu überwachen, wäre daran interessiert, seine Software so zu gestalten, dass sie etwas Ungewöhnliches erkennt. Analysten, die aggregierte Gesundheitsdaten analysiert haben, können den Produktentwicklern dabei helfen, die richtigen Algorithmen zu finden, um zu erkennen und Alarm auszulösen, wenn sich bestimmte Daten nicht normal entwickeln.

### **Identifizierung von Themen**

UX-Designer sind möglicherweise auf Analysten angewiesen, um Daten zur Interaktivität der Nutzer zu analysieren. Ähnlich wie bei Problemen, bei denen Analysten Dinge kategorisieren müssen, kann es bei Projekten zur Verbesserung der Benutzerfreundlichkeit erforderlich sein, dass Analysten Themen identifizieren, um die richtigen Produkteigenschaften für Verbesserungen zu priorisieren. Themen werden am häufigsten verwendet, um Forschern zu helfen, bestimmte Aspekte von Daten zu untersuchen. In einer Nutzerstudie sind die Überzeugungen, Praktiken und Bedürfnisse der Nutzer Beispiele für Themen.

Vielleicht fragen Sie sich jetzt, ob es einen Unterschied zwischen der Kategorisierung von Dingen und der Identifizierung von Themen gibt. Der beste Weg, darüber nachzudenken, ist folgender: Bei der Kategorisierung von Dingen werden Elemente in Kategorien eingeteilt; bei der Identifizierung von Themen gehen wir einen Schritt weiter, indem wir diese Kategorien zu umfassenderen Themen zusammenfassen.

### **Entdeckung von Verbindungen**

Ein Logistikunternehmen, das mit einem anderen Unternehmen zusammenarbeitet, um Sendungen rechtzeitig an die Kunden auszuliefern, ist ein Problem, bei dem Analysten Zusammenhänge erkennen müssen. Durch die Analyse der Wartezeiten an den Versand-Hubs können Analysten die geeigneten Änderungen im Zeitplan ermitteln, um die Anzahl der pünktlichen Lieferungen zu erhöhen.

### **Finden von Mustern**

Die Minimierung der durch Maschinenausfälle verursachten Ausfallzeiten ist ein Beispiel für ein Problem, bei dem Analysten Muster in Daten finden müssen. Durch die Analyse von Wartungsdaten könnten sie zum Beispiel herausfinden, dass die meisten Ausfälle auftreten, wenn die regelmäßige Wartung um mehr als ein 15-Tage-Fenster verschoben wird.

## Schlüssel zum Erfolg

Im Laufe dieses Programms werden Sie einen schärferen Blick für Probleme entwickeln und üben, die Problemtypen zu durchdenken, wenn Sie Ihre Analyse beginnen. Diese Methode der Problemlösung wird Ihnen helfen, Lösungen zu finden, die den Bedürfnissen aller Stakeholder gerecht werden.

---
