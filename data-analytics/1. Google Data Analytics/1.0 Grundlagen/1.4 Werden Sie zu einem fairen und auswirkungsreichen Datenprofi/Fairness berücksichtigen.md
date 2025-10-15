---
autor: Simon Janke
title: Fairness berücksichtigen
type: Google Data Analytics Kurs
date: 2025-10-14
tags:
  - fairness
links:
  - "[[Fairness]]"
  - "[[Grundlagen]]"
---
---
# Fairness berücksichtigen

Sie haben bereits gelernt, dass ein Teil der Verantwortung eines Datenexperten darin besteht, dafür zu sorgen, dass seine Analyse fair ist. **Fairness** bedeutet, dass Sie sicherstellen müssen, dass Ihre Analyse keine Voreingenommenheit hervorruft oder verstärkt. Das kann eine Herausforderung sein, aber wenn die Analyse nicht objektiv ist, können die Schlussfolgerungen irreführend und sogar schädlich sein. In dieser Lektüre werden Sie einige bewährte Praktiken kennenlernen, die Sie bei Ihrer Arbeit für eine faire Analyse nutzen können!

## Fairness berücksichtigen

Im Folgenden finden Sie einige Strategien, die eine faire Analyse unterstützen:

|**Bewährte Methode**|**Erläuterung**|**Beispiel**|
|---|---|---|
|Berücksichtigen Sie alle verfügbaren Daten|Ein Teil Ihrer Aufgabe als Fachkraft für Datenanalyse besteht darin, herauszufinden, welche Daten für Ihre Analyse nützlich sein werden. Oft gibt es Daten, die für das, worauf Sie sich konzentrieren, nicht relevant sind oder nicht mit Ihren Erwartungen übereinzustimmen scheinen. Aber Sie können sie nicht einfach ignorieren. Es ist wichtig, alle verfügbaren Daten zu berücksichtigen, damit Ihre Analyse die Wahrheit widerspiegelt und nicht nur Ihre eigenen Erwartungen.|Das Verkehrsministerium eines Bundesstaates ist daran interessiert, die Verkehrsmuster an Feiertagen zu messen. Zunächst werden nur Metriken zum Verkehrsaufkommen und zur Tatsache, dass es sich um Feiertage handelt, berücksichtigt. Aber das Daten-Team stellt fest, dass es nicht bedacht hat, wie sich das Wetter an diesen Feiertagen auf das Verkehrsvolumen auswirken könnte. Die Berücksichtigung dieser zusätzlichen Daten hilft ihnen, umfassendere Statistiken zu erhalten.|
|Identifizieren Sie umgebende Faktoren|Wie Sie in diesen Kursen lernen werden, ist der Kontext für Sie und Ihre Stakeholder der Schlüssel zum Verständnis der endgültigen Schlussfolgerungen einer Analyse. So wie Sie alle Daten berücksichtigen, müssen Sie auch die umgebenden Faktoren verstehen, die Einfluss auf die gewonnenen Statistiken haben könnten.|Eine Personalabteilung möchte die Urlaubszeit ihrer Mitarbeiter besser planen, um den Personalbedarf vorauszusehen. Die Personalabteilung verwendet eine Liste der nationalen Feiertage als Schlüssel für den Prozess der Datenerfassung. Dabei werden jedoch wichtige Feiertage, die nicht im Bankkalender stehen, nicht berücksichtigt, was zu einer Voreingenommenheit gegenüber Mitarbeitern führt, die diese Feiertage feiern. Außerdem erhält die Personalabteilung dadurch weniger nützliche Ergebnisse, da die Feiertage nicht unbedingt auf die tatsächliche Mitarbeiterpopulation zutreffen.|
|Berücksichtigen Sie selbst gemeldete Daten|**Selbstauskunft** ist eine Technik der Datenerhebung, bei der die Teilnehmer Informationen über sich selbst angeben. Selbstauskünfte können eine gute Möglichkeit sein, Fairness in Ihren Prozess der Datenerhebung zu bringen. Menschen bringen bewusste und unbewusste Voreingenommenheit in ihre Beobachtungen über die Welt ein, auch über andere Menschen. Die Verwendung von Selbstauskünften bei der Datenerhebung kann dazu beitragen, diese Voreingenommenheit der Beobachter zu vermeiden. Darüber hinaus bietet die Trennung der selbstberichteten Daten von anderen Daten, die Sie sammeln, einen wichtigen Kontext für Ihre Schlussfolgerungen!|Eine Fachkraft für Datenanalyse arbeitet an einem Projekt für einen stationären Einzelhändler. Sein Ziel ist es, mehr über seine Kunden zu erfahren. Diese Fachkraft für Datenanalyse weiß, dass sie bei der Datenerfassung auf Fairness achten muss. Sie beschließt, eine Umfrage zu erstellen, in der die Kunden Informationen über sich selbst angeben können. Auf diese Weise vermeiden sie Voreingenommenheiten, die bei anderen Methoden zur Erhebung demografischer Daten auftreten können. Wenn sie zum Beispiel die Vertriebsmitarbeiter ihre Beobachtungen über die Kunden berichten lassen würden, könnten sie unbewusste Voreingenommenheiten der Mitarbeiter in die Daten einbringen.|
|Nutzen Sie Oversampling effektiv|Wenn Sie Daten über eine Population erheben, ist es wichtig, dass Sie die tatsächliche Zusammensetzung dieser Population kennen. Manchmal kann ein Oversampling Ihnen dabei helfen, Gruppen in der Population zu repräsentieren, die sonst nicht fair vertreten wären. **Oversampling** ist der Prozess, bei dem die Stichprobengröße der nicht dominanten Gruppen in einer Population erhöht wird. So können Sie sie besser repräsentieren und unausgewogene Datasets korrigieren.|Ein Fitnessunternehmen gibt neue digitale Inhalte für Nutzer seiner Geräte heraus. Sie sind daran interessiert, Inhalte zu entwerfen, die verschiedene Nutzer ansprechen, da sie wissen, dass verschiedene Personen auf unterschiedliche Weise mit ihren Geräten interagieren können. Ein Teil der Nutzer ist zum Beispiel 70 Jahre oder älter. Um diese Nutzer zu repräsentieren, nehmen sie eine Überstichprobe in ihre Daten auf. Auf diese Weise werden die Entscheidungen, die sie über ihre Fitness-Inhalte treffen, umfassender sein.|
|Denken Sie an Fairness von Anfang bis Ende|Um sicherzustellen, dass Ihre Analyse und Ihre endgültigen Schlussfolgerungen fair sind, sollten Sie von den frühesten Stadien eines Projekts an bis zu dem Zeitpunkt, an dem Sie die Ergebnisse der Statistiken umsetzen, auf Fairness achten. Das bedeutet, dass die Datenerfassung, -bereinigung, -verarbeitung und -analyse unter dem Gesichtspunkt der Fairness durchgeführt werden.|Ein Datenteam beginnt ein Projekt, indem es Fairness-Maßnahmen in seinen Prozess der Datenerhebung einbezieht. Zu diesen Maßnahmen gehören eine Überstichprobe der Population und die Verwendung von Selbstauskünften. Sie versäumen es jedoch, die Stakeholder bei der Präsentation über diese Maßnahmen zu informieren. Infolgedessen haben die Stakeholder ein verzerrtes Verständnis der Daten. Aus dieser Erfahrung lernen sie und fügen Schlüsselinformationen über Fairness-Erwägungen zu zukünftigen Präsentationen für Stakeholder hinzu.|

## Die wichtigsten Erkenntnisse

Als Datenexperte müssen Sie sicherstellen, dass Sie immer auf Fairness achten. So können Sie vermeiden, dass Sie Voreingenommenheit erzeugen oder verstärken oder versehentlich irreführende Schlussfolgerungen ziehen. Die Anwendung dieser Best Practices kann Ihnen bei Ihrer Analyse helfen und Sie zu einem besseren Datenexperten machen!

---
