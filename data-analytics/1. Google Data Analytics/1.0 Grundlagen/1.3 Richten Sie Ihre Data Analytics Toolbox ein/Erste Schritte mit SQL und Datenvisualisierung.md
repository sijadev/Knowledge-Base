---
autor: Simon Janke
title: Erste Schritte mit SQL und Datenvisualisierung
type: Google Data Analytics Kurs
date: 2025-10-10
tags:
  - sql
  - datenvisualisierung
links:
  - "[[Grundlagen]]"
  - "[[6.1.2 Grundlagen Kurs 1 - Modul 3]]"
---

---

## SQL in Aktion

**Daten:**

- speichern
- organisieren
- analysieren

**Abfrage (Query):**

- Eine Abfrage ist eine Anfrage nach Daten oder Informationen aus einer Datenbank

Basic structure of a query:

    Der Aufbau: Spalten --> Tabelle --> Konditionen (Bedingungen)

SELECT  <br>
    - Auswahl der Spalten <br>
FROM  <br>
    - Auswahl der Table  <br>
WHERE  <br>
    - Mit einer bestimmten Bedingung  <br>

### **Beispiel für eine Abfrage**

So würde eine einfache Abfrage in BigQuery, einem Data Warehouse auf der Google
Cloud Plattform, aussehen.

```sql
SELECT first_name

FROM customer_data.customer_name

WHERE first_name = 'Tony'
```text

Die obige Abfrage verwendet drei Befehle, um Kunden mit der first_name, 'Tony'
zu finden

#### Unendliche SQL-Möglichkeiten

Sie haben gelernt, dass eine SQL-Abfrage SELECT, FROM und WHERE verwendet, um
die Daten anzugeben, die von der Abfrage zurückgegeben werden sollen. In dieser
Lektüre finden Sie genauere Informationen über die Formatierung von Abfragen,
die Verwendung von WHERE Bedingungen, die Auswahl aller Spalten in einer
Tabelle, das Hinzufügen von Kommentaren und die Verwendung von Aliasen. All
dies erleichtert Ihnen das Verständnis (und das Schreiben) von Abfragen, um SQL
in die Praxis umzusetzen. Im letzten Abschnitt dieser Lektüre finden Sie ein
Beispiel dafür, was eine Fachkraft für Datenanalyse tun würde, um
Mitarbeiterdaten für ein Projekt abzurufen.

### Großschreibung, Einrückung und Semikolon

Sie können Ihre SQL-Abfragen in Kleinbuchstaben schreiben und müssen sich keine
Gedanken über zusätzliche Leerzeichen zwischen den Wörtern machen. Die
Verwendung von Großbuchstaben und Einrückungen kann jedoch dazu beitragen, dass
Sie die Informationen leichter lesen können. Wenn Sie Ihre Abfragen
übersichtlich halten, können Sie sie später leichter überprüfen oder
Fehlerbehebungen vornehmen, wenn Sie sie überprüfen müssen.

```sql
SELECT field1

FROM table

WHERE field1 = condition;
```text

Beachten Sie, dass die oben gezeigte SQL-Anweisung ein Semikolon am Ende hat.
Das Semikolon ist ein Anweisungsende und Teil des SQL-92-Standards des American
National Standards Institute (ANSI), einer empfohlenen gemeinsamen Syntax für
die Akzeptanz durch alle SQL-Datenbanken. Allerdings haben nicht alle
SQL-Datenbanken das Semikolon übernommen oder setzen es durch. Es ist also
möglich, dass Sie auf einige SQL-Anweisungen stoßen, die nicht mit einem
Semikolon abgeschlossen werden. Wenn eine Anweisung ohne Semikolon
funktioniert, ist sie in Ordnung.

### WHERE-Bedingungen

In der oben gezeigten Abfrage identifiziert die SELECT Klausel die Spalte, aus
der Sie Daten beziehen möchten, mit dem Namen field1, und die FROM Klausel
identifiziert die table, in der sich die Spalte befindet, mit dem Namen table.
Schließlich schränkt die WHERE Klausel Ihre Abfrage ein, so dass die Datenbank
nur die Daten mit einer exakten Wertübereinstimmung oder die Daten zurückgibt,
die einer bestimmten Bedingung entsprechen, die Sie erfüllen möchten.

Wenn Sie zum Beispiel nach einem bestimmten Kunden mit dem Nachnamen Chavez
suchen, würde die WHERE Klausel lauten:
```sql
WHERE field1 = 'Chavez'
```text
Wenn Sie jedoch nach allen Kunden mit einem Nachnamen suchen, der mit den
Buchstaben "Ch" beginnt, würde die WHERE Klausel lauten:
```sql
WHERE field1 LIKE 'Ch%'
```text
Sie können daraus schließen, dass die LIKE Klausel sehr mächtig ist, weil Sie
damit der Datenbank sagen können, dass sie nach einem bestimmten Muster suchen
soll! Das Prozentzeichen % wird als Platzhalter verwendet, um mit einem oder
mehreren Zeichen übereinzustimmen. In dem obigen Beispiel würden sowohl
**Chavez** als auch **Chen** zurückgegeben werden. Beachten Sie, dass in
einigen Datenbanken ein Sternchen * als Platzhalter anstelle des
Prozentzeichens % verwendet wird.

### SELECT alle Spalten

Können Sie SELECT * verwenden?

Wenn Sie im Beispiel SELECT field1 durch SELECT * ersetzen, würden Sie alle
Spalten der Tabelle auswählen, anstatt nur die Spalte field1. Von der Syntax
her handelt es sich um eine korrekte SQL-Anweisung, aber Sie sollten das
Sternchen * sparsam und mit Bedacht verwenden. Je nachdem, wie viele Spalten
eine Tabelle hat, könnten Sie eine enorme Menge an Daten auswählen. Die Auswahl
von zu vielen Daten kann dazu führen, dass eine Abfrage langsam läuft.

### Kommentare

Einige Tabellen sind nicht mit ausreichend aussagekräftigen Namenskonventionen
versehen. In unserem Beispiel war field1 die Spalte für den Nachnamen eines
Kunden, aber Sie würden sie nicht an ihrem Namen erkennen. Ein besserer Name
wäre z.B. last_name gewesen. In diesen Fällen können Sie neben Ihrem SQL
Kommentare einfügen, damit Sie sich besser an den Namen erinnern können.
Kommentare sind Text, der zwischen bestimmten Zeichen, /* und */, oder nach
zwei Bindestrichen --) eingefügt wird, wie unten gezeigt.

```sql
    table -- this is the customer data table

WHERE

    field1 LIKE 'Ch%';
```text
Kommentare können sowohl außerhalb einer Anweisung als auch innerhalb einer
Anweisung eingefügt werden. Sie können diese Flexibilität nutzen, um eine
allgemeine Beschreibung dessen zu geben, was Sie vorhaben, Schritt für Schritt
zu beschreiben, wie Sie es erreichen und warum Sie verschiedene
Parameter/Bedingungen festlegen.

```sql
-- This is an important query used later to join with the accounts table

SELECT

        rowkey,  -- key used to join with account_id

Info.date,  -- date is in string format YYYY-MM-DD HH:MM:SS

Info.code  -- e.g., 'pub-###'

FROM  Publishers
```text
Je vertrauter Sie mit SQL werden, desto einfacher wird es, Abfragen auf einen
Blick zu lesen und zu verstehen. Dennoch schadet es nie, Kommentare in eine
Abfrage einzufügen, um sich daran zu erinnern, was Sie eigentlich tun wollen.
Das macht es auch für andere einfacher, Ihre Abfrage zu verstehen, wenn sie
weitergegeben wird. Da Ihre Abfragen immer komplexer werden, wird Ihnen diese
Praxis viel Zeit und Energie sparen, um komplexe Abfragen zu verstehen, die Sie
vor Monaten oder Jahren geschrieben haben.

### **Beispiel für eine Abfrage mit Kommentaren**

Hier ist ein Beispiel dafür, wie Kommentare in BigQuery geschrieben werden
können:

```sql
    customer_data.customer_name
```text
Im obigen Beispiel wurde vor der SQL-Anweisung ein Kommentar eingefügt, um zu
erklären, was die Abfrage bewirkt. Außerdem wurde neben jedem Spaltennamen ein
Kommentar eingefügt, um die Spalte und ihre Verwendung zu beschreiben. Zwei
Bindestriche -- werden im Allgemeinen unterstützt. Es ist also am besten, -- zu
verwenden und damit konsistent zu sein. Sie können # anstelle von -- in der
obigen Abfrage verwenden, aber # wird nicht in allen SQL Versionen erkannt;
MySQL erkennt beispielsweise # nicht an. Sie können auch Kommentare zwischen /*
und */ setzen, wenn die von Ihnen verwendete Datenbank dies unterstützt.

Wenn Sie sich beruflich weiterentwickeln, können Sie je nach SQL-Datenbank, die
Sie verwenden, die von Ihnen bevorzugten Trennzeichen für Kommentare auswählen
und diese als einheitlichen Stil beibehalten. Wenn Ihre Abfragen immer
komplexer werden, werden Sie durch das Hinzufügen hilfreicher Kommentare viel
Zeit und Energie sparen, um Abfragen zu verstehen, die Sie vielleicht schon vor
Monaten oder Jahren geschrieben haben.

### Aliases

Sie können es sich auch einfacher machen, indem Sie den Spalten- oder
Tabellennamen einen neuen Namen oder **Alias** zuweisen, um die Arbeit damit zu
erleichtern (und die Notwendigkeit von Kommentaren zu vermeiden). Dies
geschieht mit einer SQL AS-Klausel. In dem folgenden Beispiel werden Aliasnamen
sowohl für einen Tabellennamen als auch für eine Spalte verwendet. In der
Datenbank heißt die Tabelle actual_table_name und die Spalte in dieser Tabelle
heißt actual_column_name. Sie werden als my_table_alias bzw. my_column_alias
aliasiert. Diese Aliase sind nur für die Dauer der Abfrage gültig. Ein Alias
ändert nicht den tatsächlichen Namen einer Spalte oder Tabelle in der
Datenbank.

### **Beispiel für eine Abfrage mit Aliasen**

```sql
SELECT

    my_table_alias.actual_column_name AS my_column_alias

FROM

    actual_table_name AS my_table_alias
```text

### Einsatz von SQL als Fachkraft für Datenanalyse

Stellen Sie sich vor, Sie sind Fachkraft für Datenanalyse in einem kleinen
Unternehmen und Ihr Vorgesetzter bittet Sie um einige Mitarbeiterdaten. Sie
beschließen, eine Abfrage mit SQL zu schreiben, um das, was Sie brauchen, aus
der Datenbank zu holen.

Sie möchten alle Spalten abfragen: **empID, Vorname, Nachname, jobCode** und
**Gehalt.** Da Sie wissen, dass die Datenbank nicht sehr groß ist, geben Sie
nicht jeden Spaltennamen in die SELECT Klausel ein, sondern verwenden SELECT *.
Damit werden alle Spalten aus der Tabelle Employee in der FROM Klausel
ausgewählt.

```sql
SELECT

    *

FROM

    Employee
```text
Jetzt können Sie die Daten, die Sie aus der Tabelle **Employee** benötigen,
genauer bestimmen. Wenn Sie alle Daten über Mitarbeiter mit dem Stellencode
'SFI' haben möchten, können Sie eine WHERE Klausel verwenden, um die Daten auf
der Grundlage dieser zusätzlichen Anforderung herauszufiltern.

Hier verwenden Sie:

```sql
SELECT

    *

FROM

    Employee

WHERE

    jobCode = 'SFI'
```text

Ein Teil der Daten, die von der SQL-Abfrage zurückgegeben werden, könnte wie
folgt aussehen:

|**empID**|**vorname**|**nachname**|**jobCode**|**gehalt**|
|---|---|---|---|---|
|0002|Homer|Simpson|SFI|15000|
|0003|Marge|Simpson|SFI|30000|
|0034|Bart|Simpson|SFI|25000|
|0067|Lisa|Simpson|SFI|38000|
|0088|Ned|Flandern|SFI|42000|
|0076|Barney|Gumble|SFI|32000|

Angenommen, Sie bemerken einen großen Bereich für den Stellencode 'SFI'. Sie
möchten vielleicht alle Mitarbeiter in allen Abteilungen mit niedrigeren
Gehältern für Ihren Manager markieren. Da auch Praktikanten in der Tabelle
enthalten sind, deren Gehalt unter 30.000 $ liegt, möchten Sie sicherstellen,
dass Ihre Ergebnisse nur die Vollzeitbeschäftigten mit einem Gehalt von 30.000
$ oder weniger enthalten. Mit anderen Worten: Sie möchten Praktikanten mit dem
Stellencode 'INT' ausschließen, die ebenfalls weniger als 30.000 $ verdienen.
Mit der AND Klausel können Sie auf beide Bedingungen testen.

Sie erstellen eine SQL-Abfrage ähnlich der folgenden, wobei <> für "ist nicht
gleich" steht:

```sql
SELECT

    *

FROM

    Employee

WHERE

    jobCode <> 'INT'

      AND salary <= 30000;
```text

Die aus der SQL-Abfrage resultierenden Daten könnten wie folgt aussehen
(Praktikanten mit dem Stellencode **INT** werden nicht zurückgegeben):

|**empID**|**vorname**|**nachname**|**jobCode**|**gehalt**|
|---|---|---|---|---|
|0002|Homer|Simpson|SFI|15000|
|0003|Marge|Simpson|SFI|30000|
|0034|Bart|Simpson|SFI|25000|
|0108|Edna|Krabappel|TUL|18000|
|0099|Moe|Szyslak|ANA|28000|

Mit einem schnellen Zugriff auf diese Art von Daten mit Hilfe von SQL können
Sie Ihrem Manager eine Menge verschiedener Statistiken über Mitarbeiterdaten
zur Verfügung stellen, einschließlich der Frage, ob die Gehälter der
Mitarbeiter im gesamten Unternehmen angemessen sind. Glücklicherweise zeigt die
Abfrage, dass nur zwei weitere Mitarbeiter eine Gehaltsanpassung benötigen, und
Sie teilen die Ergebnisse mit Ihrem Vorgesetzten.

Wenn Sie die Daten abrufen, analysieren und eine Lösung implementieren, können
Sie letztendlich die Zufriedenheit und Loyalität Ihrer Mitarbeiter verbessern.
Das macht SQL zu einem ziemlich mächtigen Werkzeug.

### Ressourcen, um mehr zu erfahren

Nicht-Abonnenten können auf diese Ressourcen kostenlos zugreifen. Wenn eine
Website jedoch die Anzahl der kostenlosen Artikel pro Monat begrenzt und Sie
Ihr Limit bereits erreicht haben, sollten Sie die Ressource als Lesezeichen
speichern und später darauf zurückkommen.

- [W3Schools SQL-Tutorial](https://www.w3schools.com/sql/default.asp "W3Schools SQL Tutorial"): Wenn Sie ein ausführliches Tutorial zu SQL erkunden möchten, ist dies der perfekte Ausgangspunkt. Dieses Tutorial enthält interaktive Beispiele, die Sie bearbeiten, testen und nachbauen können. Nutzen Sie es als Referenz oder vervollständigen Sie das gesamte Tutorial, um die Verwendung von SQL zu üben. Klicken Sie auf die grüne Schaltfläche **SQL jetzt lernen** oder auf die Schaltfläche **Weiter** , um mit dem Lernprogramm zu beginnen.

- [SQL-Spickzettel](https://www.sqltutorial.org/sql-cheat-sheet/ "SQL Cheat Sheet"): Wenn Sie fortgeschrittener sind, können Sie sich mit dieser praktischen 3-seitigen Ressource einen Überblick über zusätzliche SQL-Funktionen und -Formeln verschaffen. Wenn Sie den Spickzettel durchgelesen haben, werden Sie viel mehr über die verschiedenen SQL-Techniken wissen und darauf vorbereitet sein, sie für Unternehmensanalysen und andere Aufgaben einzusetzen.

### Die wichtigsten Erkenntnisse

SQL-Abfragen verwenden SELECT, FROM und WHERE, um die Daten anzugeben, die von
der Abfrage zurückgegeben werden sollen. Großschreibung, Einrückung und
Semikolons sind nützlich, um Ihre SQL Abfragen leichter lesbar zu machen.
Darüber hinaus können Sie Kommentare hinzufügen, um Abfragen für andere zu
erläutern. Im weiteren Verlauf dieses Kurses werden Sie viele Möglichkeiten
entdecken, wie SQL ein sehr leistungsfähiges Tool zum Abrufen, Analysieren und
Interpretieren von Daten sein kann.

#### Werden Sie ein Daten-Vizzer

#### Planen Sie eine Datenvisualisierung

### Schritte zur Planung einer Datenvisualisierung

Gehen wir ein Beispiel für eine reale Situation durch, in der eine Fachkraft
für Datenanalyse eine Datenvisualisierung erstellen muss, um sie mit
Stakeholdern zu teilen. Stellen Sie sich vor, Sie sind Fachkraft für
Datenanalyse bei einem Bekleidungshändler. Das Unternehmen hilft kleinen
Bekleidungsgeschäften bei der Verwaltung ihrer Bestände, und die Umsätze
boomen. Eines Tages erfahren Sie, dass Ihr Unternehmen eine umfassende
Aktualisierung seiner Website plant. Um Entscheidungen für die Aktualisierung
der Website zu treffen, sollen Sie die Daten der bestehenden Website und die
Datensätze der Verkäufe analysieren. Gehen wir die Schritte durch, die Sie
befolgen könnten.

### Schritt 1: Untersuchen Sie die Daten auf Muster

Zunächst bitten Sie Ihren Manager oder den Dateneigentümer um Zugang zu den
aktuellen Datensätzen und Berichten zur Website-Analyse. Dazu gehören
Informationen darüber, wie sich die Kunden auf der bestehenden Website des
Unternehmens verhalten, grundlegende Informationen darüber, wer sie besucht
hat, wer bei dem Unternehmen gekauft hat und wie viel sie gekauft haben.

Bei der Durchsicht der Daten fällt Ihnen ein Muster bei denjenigen auf, die die
Website des Unternehmens am häufigsten besuchen: geografische Herkunft und
höhere Kaufbeträge. Bei einer weiteren Analyse könnten diese Informationen
erklären, warum die Verkäufe im Nordosten derzeit so stark sind - und Ihrem
Unternehmen dabei helfen, Wege zu finden, sie durch die neue Website noch
weiter zu steigern.

### Schritt 2: Planen Sie Ihre Visualisierungen

Als nächstes ist es an der Zeit, die Daten zu verfeinern und die Ergebnisse
Ihrer Analyse zu präsentieren. RIGHT: Sie haben eine Menge Daten, die auf
verschiedene Tabellen verteilt sind, was nicht gerade ideal ist, um Ihre
Ergebnisse mit dem Management und dem Marketing Team zu teilen. Sie möchten
eine Datenvisualisierung erstellen, die Ihre Ergebnisse schnell und effektiv
für Ihre Zielgruppe erklärt. Da Sie wissen, dass Ihre Zielgruppe
vertriebsorientiert ist, wissen Sie bereits, dass die Datenvisualisierung, die
Sie verwenden, dies auch sein sollte:

- Umsatzzahlen im Zeitverlauf zeigen

- Verkäufe mit dem Standort verknüpfen

- Die Beziehung zwischen Umsatz und Website-Nutzung aufzeigen

- Zeigen, welche Kunden das Wachstum ankurbeln

### Schritt 3: Erstellen Sie Ihre Visualisierungen

Nachdem Sie nun entschieden haben, welche Art von Informationen und Statistiken
Sie anzeigen möchten, ist es an der Zeit, mit der Erstellung der eigentlichen
Visualisierungen zu beginnen. Denken Sie daran, dass die Erstellung der
richtigen Visualisierung für eine Präsentation oder zum Austausch mit
Stakeholdern ein Prozess ist. Sie müssen verschiedene Visualisierungsformate
ausprobieren und Anpassungen vornehmen, bis Sie die gewünschte Darstellung
erhalten. In diesem Fall ist eine Mischung aus verschiedenen Visualisierungen
am besten geeignet, um Ihre Ergebnisse zu kommunizieren und Ihre Analyse in
eine überzeugende Story für Stakeholder zu verwandeln. Sie können also die
integrierten Diagramm-Funktionen in Ihren Tabellen nutzen, um die Daten zu
organisieren und Ihre Visualisierungen zu erstellen.

### Erstellen Sie Ihr Toolkit für die Datenvisualisierung

Für die Datenvisualisierung stehen Ihnen viele verschiedene Tools zur Verfügung.

- Sie können die Tools zur Visualisierung in Ihrer Tabelle verwenden, um einfache Visualisierungen wie Linien- und Balkendiagramme zu erstellen.

- Mit fortgeschritteneren Tools wie Tableau können Sie Daten in Visualisierungen im Dashboard-Stil integrieren.

- Wenn Sie mit der Programmiersprache R arbeiten, können Sie die Visualisierungstools in RStudio verwenden.

Die Wahl der Visualisierung hängt von einer Vielzahl von Treibern ab, z. B. von
der Größe Ihrer Daten und dem Prozess, den Sie für die Analyse Ihrer Daten
verwendet haben (Tabelle, Datenbanken/Abfragen oder Programmiersprachen).
Betrachten wir zunächst nur die Grundlagen.

### Tabellenkalkulationen (Microsoft Excel oder Google Sheets)

In unserem Beispiel haben die integrierten Diagramme und Grafiken in
Tabellenkalkulationen den Prozess der Visualisierung schnell und einfach
gemacht. Tabellen eignen sich hervorragend für die Erstellung einfacher
Visualisierungen wie Balkendiagramme und Kreisdiagramme und bieten sogar einige
fortgeschrittene Visualisierungen wie Karten, Wasserfall- und Trichterdiagramme
(siehe die folgenden Abbildungen).

Manchmal benötigen Sie jedoch ein leistungsfähigeres Tool, um Ihre Daten
wirklich zum Leben zu erwecken. Tableau und RStudio sind zwei Beispiele für
weit verbreitete Plattformen, die Sie bei der Planung, Erstellung und
Präsentation effektiver und überzeugender Datenvisualisierungen unterstützen
können.

### Software zur Visualisierung (Tableau)

Tableau ist ein beliebtes Tool zur Datenvisualisierung, mit dem Sie Daten aus
nahezu jedem System abrufen und in aussagekräftige Grafiken oder umsetzbare
Statistiken verwandeln können. Die Plattform bietet integrierte visuelle Best
Practices, die die Analyse und den Austausch von Daten schnell, einfach und
(vor allem) nützlich machen. Tableau eignet sich für eine Vielzahl von Daten
und verfügt über ein interaktives Dashboard, mit dem Sie und Ihre Stakeholder
die Daten per Mausklick interaktiv erkunden können.

Sie können mit Tableau über das
[Video-Anleitung](https://public.tableau.com/en-us/s/resources "How-to Video")
ressourcen. Tableau Public ist kostenlos, einfach zu benutzen und voller
hilfreicher Informationen. Die Seite Ressourcen ist eine zentrale Anlaufstelle
für Anleitungsvideos, Beispiele und Datasets, mit denen Sie üben können. Um zu
erfahren, was andere Fachkräfte für Datenanalyse auf Tableau teilen, besuchen
Sie die Seite [Viz des
Tages](https://public.tableau.com/en-us/gallery/?tab=viz-of-the-day&type=viz-of-the-day
"Viz of the Day") seite, wo Sie wunderschöne Visualisierungen finden, von einem
Überblick über die [Leuchttürme
Griechenlands](https://public.tableau.com/app/profile/george.koursaros/viz/LighthousesofGreece/Lighthouses)
bis hin zu [Wer redet in beliebten
Filmen](https://public.tableau.com/app/profile/bo.mccready8742/viz/WordDataWorking/WhoIsTalking
"Who’s Talking in Popular Films").

### Programmiersprache (R mit RStudio)

Viele Fachkräfte für Datenanalyse arbeiten mit der Programmiersprache R. Die
meisten, die mit R arbeiten, verwenden auch RStudio, eine Integrierte
Entwicklungsumgebung (IDE), für ihre Datenvisualisierung. Wie bei Tableau
können Sie mit RStudio Datenvisualisierungen im Dashboard-Stil erstellen.

---
