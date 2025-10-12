---
autor: Simon Janke
title: SQL Cheat Sheet
type: Ressource
date: 2025-10-12
tags:
  - SQL
  - cheat-sheet
  - BigQuery
  - referenz
---

# 📊 SQL Cheat Sheet für Data Analysts

---

## 🎯 Grundlegende SELECT-Abfragen

### Alle Spalten auswählen
```sql
SELECT * 
FROM table_name;
```

### Bestimmte Spalten auswählen
```sql
SELECT column1, column2, column3
FROM table_name;
```

### Mit LIMIT (erste N Zeilen)
```sql
SELECT * 
FROM table_name
LIMIT 10;
```

### DISTINCT (Duplikate entfernen)
```sql
SELECT DISTINCT country
FROM customers;
```

---

## 🔍 WHERE - Filtern von Daten

### Einfache Bedingungen
```sql
-- Gleich
SELECT * FROM customers WHERE country = 'Germany';

-- Nicht gleich
SELECT * FROM customers WHERE country != 'Germany';
SELECT * FROM customers WHERE country <> 'Germany';

-- Größer/Kleiner
SELECT * FROM orders WHERE total_amount > 1000;
SELECT * FROM orders WHERE order_date >= '2025-01-01';

-- NULL Werte
SELECT * FROM customers WHERE email IS NULL;
SELECT * FROM customers WHERE email IS NOT NULL;
```

### Kombinierte Bedingungen
```sql
-- AND (beide Bedingungen müssen erfüllt sein)
SELECT * FROM orders 
WHERE total_amount > 1000 
AND country = 'Germany';

-- OR (eine der Bedingungen muss erfüllt sein)
SELECT * FROM customers 
WHERE country = 'Germany' 
OR country = 'Austria';

-- IN (Wert in Liste)
SELECT * FROM customers 
WHERE country IN ('Germany', 'Austria', 'Switzerland');

-- NOT IN
SELECT * FROM customers 
WHERE country NOT IN ('USA', 'Canada');

-- BETWEEN (Wertebereich)
SELECT * FROM orders 
WHERE order_date BETWEEN '2025-01-01' AND '2025-12-31';

-- LIKE (Mustersuche)
SELECT * FROM customers 
WHERE email LIKE '%@gmail.com';

-- Wildcards:
-- % = beliebig viele Zeichen
-- _ = genau ein Zeichen

-- Beginnt mit 'A'
SELECT * FROM customers WHERE name LIKE 'A%';

-- Endet mit 'son'
SELECT * FROM customers WHERE name LIKE '%son';

-- Enthält 'and'
SELECT * FROM customers WHERE name LIKE '%and%';
```

---

## 📊 Aggregationsfunktionen

### Grundlegende Aggregationen
```sql
-- Anzahl
SELECT COUNT(*) FROM orders;
SELECT COUNT(customer_id) FROM orders;
SELECT COUNT(DISTINCT customer_id) FROM orders; -- Einzigartige Kunden

-- Summe
SELECT SUM(total_amount) FROM orders;

-- Durchschnitt
SELECT AVG(total_amount) FROM orders;

-- Minimum/Maximum
SELECT MIN(total_amount) FROM orders;
SELECT MAX(total_amount) FROM orders;
```

### Kombinierte Aggregationen
```sql
SELECT 
  COUNT(*) AS order_count,
  SUM(total_amount) AS total_revenue,
  AVG(total_amount) AS avg_order_value,
  MIN(total_amount) AS min_order,
  MAX(total_amount) AS max_order
FROM orders
WHERE order_date >= '2025-01-01';
```

---

## 📦 GROUP BY - Gruppierung

### Einfache Gruppierung
```sql
-- Anzahl Bestellungen pro Land
SELECT 
  country,
  COUNT(*) AS order_count
FROM orders
GROUP BY country;

-- Umsatz pro Monat
SELECT 
  DATE_TRUNC(order_date, MONTH) AS month,
  SUM(total_amount) AS monthly_revenue
FROM orders
GROUP BY month
ORDER BY month;
```

### Mehrfache Gruppierung
```sql
-- Umsatz pro Land und Kategorie
SELECT 
  country,
  category,
  SUM(total_amount) AS revenue
FROM orders
GROUP BY country, category
ORDER BY country, revenue DESC;
```

### HAVING (Filter nach Aggregation)
```sql
-- Nur Länder mit mehr als 100 Bestellungen
SELECT 
  country,
  COUNT(*) AS order_count
FROM orders
GROUP BY country
HAVING COUNT(*) > 100
ORDER BY order_count DESC;

-- Kunden mit Gesamtumsatz über 10.000€
SELECT 
  customer_id,
  SUM(total_amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(total_amount) > 10000
ORDER BY total_spent DESC;
```

---

## 🔗 JOINs - Tabellen verbinden

### INNER JOIN (nur übereinstimmende Zeilen)
```sql
SELECT 
  customers.name,
  orders.order_date,
  orders.total_amount
FROM customers
INNER JOIN orders 
  ON customers.customer_id = orders.customer_id;
```

### LEFT JOIN (alle Zeilen aus linker Tabelle)
```sql
-- Alle Kunden, auch die ohne Bestellungen
SELECT 
  customers.name,
  COUNT(orders.order_id) AS order_count
FROM customers
LEFT JOIN orders 
  ON customers.customer_id = orders.customer_id
GROUP BY customers.name;
```

### RIGHT JOIN (alle Zeilen aus rechter Tabelle)
```sql
SELECT 
  customers.name,
  orders.order_date
FROM customers
RIGHT JOIN orders 
  ON customers.customer_id = orders.customer_id;
```

### FULL OUTER JOIN (alle Zeilen aus beiden Tabellen)
```sql
SELECT 
  customers.name,
  orders.order_date
FROM customers
FULL OUTER JOIN orders 
  ON customers.customer_id = orders.customer_id;
```

### Mehrfache JOINs
```sql
SELECT 
  customers.name,
  orders.order_date,
  products.product_name,
  order_items.quantity
FROM customers
INNER JOIN orders 
  ON customers.customer_id = orders.customer_id
INNER JOIN order_items 
  ON orders.order_id = order_items.order_id
INNER JOIN products 
  ON order_items.product_id = products.product_id;
```

---

## 🎨 ORDER BY - Sortierung

```sql
-- Aufsteigend (Standard)
SELECT * FROM customers ORDER BY name;
SELECT * FROM customers ORDER BY name ASC;

-- Absteigend
SELECT * FROM customers ORDER BY name DESC;

-- Mehrere Spalten
SELECT * FROM orders 
ORDER BY country ASC, total_amount DESC;

-- Nach Position (nicht empfohlen)
SELECT name, total_amount FROM orders ORDER BY 2 DESC;
```

---

## 📅 Datumsfunktionen (BigQuery)

### Aktuelles Datum/Zeit
```sql
SELECT CURRENT_DATE() AS today;
SELECT CURRENT_DATETIME() AS now;
SELECT CURRENT_TIMESTAMP() AS timestamp;
```

### Datum extrahieren
```sql
SELECT 
  order_date,
  EXTRACT(YEAR FROM order_date) AS year,
  EXTRACT(MONTH FROM order_date) AS month,
  EXTRACT(DAY FROM order_date) AS day,
  EXTRACT(DAYOFWEEK FROM order_date) AS day_of_week
FROM orders;
```

### Datumsdifferenz
```sql
-- Tage zwischen zwei Daten
SELECT DATE_DIFF('2025-12-31', '2025-01-01', DAY) AS days;

-- Alter berechnen
SELECT 
  name,
  birth_date,
  DATE_DIFF(CURRENT_DATE(), birth_date, YEAR) AS age
FROM customers;
```

### Datum formatieren
```sql
SELECT FORMAT_DATE('%Y-%m-%d', order_date) AS formatted_date
FROM orders;

-- Formate:
-- %Y = Jahr (4-stellig)
-- %m = Monat (01-12)
-- %d = Tag (01-31)
-- %B = Monatsname (January, February, ...)
-- %A = Wochentag (Monday, Tuesday, ...)
```

### Datum gruppieren
```sql
-- Nach Monat
SELECT 
  DATE_TRUNC(order_date, MONTH) AS month,
  COUNT(*) AS orders
FROM orders
GROUP BY month
ORDER BY month;

-- Nach Quartal
SELECT 
  DATE_TRUNC(order_date, QUARTER) AS quarter,
  SUM(total_amount) AS revenue
FROM orders
GROUP BY quarter;
```

---

## 📝 String-Funktionen

```sql
-- Großbuchstaben/Kleinbuchstaben
SELECT UPPER(name) FROM customers;
SELECT LOWER(name) FROM customers;

-- Länge
SELECT LENGTH(name) FROM customers;

-- Substring
SELECT SUBSTR(name, 1, 3) FROM customers; -- Erste 3 Zeichen

-- Verknüpfen (Concatenate)
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customers;

-- Leerzeichen entfernen
SELECT TRIM(name) FROM customers;

-- Ersetzen
SELECT REPLACE(email, '@gmail.com', '@newdomain.com') FROM customers;

-- Position finden
SELECT STRPOS(email, '@') AS at_position FROM customers;
```

---

## 🔢 Mathematische Funktionen

```sql
-- Runden
SELECT ROUND(total_amount, 2) FROM orders; -- 2 Dezimalstellen

-- Aufrunden/Abrunden
SELECT CEIL(total_amount) FROM orders;
SELECT FLOOR(total_amount) FROM orders;

-- Absoluter Wert
SELECT ABS(profit) FROM orders;

-- Modulo (Rest bei Division)
SELECT order_id, order_id % 2 AS is_even FROM orders;
```

---

## 🔀 CASE WHEN - Bedingte Logik

### Einfaches CASE
```sql
SELECT 
  order_id,
  total_amount,
  CASE 
    WHEN total_amount > 1000 THEN 'High Value'
    WHEN total_amount > 500 THEN 'Medium Value'
    ELSE 'Low Value'
  END AS value_segment
FROM orders;
```

### Mehrere Bedingungen
```sql
SELECT 
  customer_id,
  country,
  total_orders,
  total_amount,
  CASE 
    WHEN country = 'Germany' AND total_amount > 5000 THEN 'VIP DE'
    WHEN country = 'Germany' THEN 'Regular DE'
    WHEN total_amount > 5000 THEN 'VIP International'
    ELSE 'Regular International'
  END AS customer_segment
FROM customer_summary;
```

---

## 🪟 Window Functions (Fortgeschritten)

### ROW_NUMBER
```sql
-- Zeilen nummerieren
SELECT 
  customer_id,
  order_date,
  total_amount,
  ROW_NUMBER() OVER (ORDER BY order_date) AS row_num
FROM orders;
```

### RANK / DENSE_RANK
```sql
-- Rangfolge erstellen
SELECT 
  customer_id,
  total_amount,
  RANK() OVER (ORDER BY total_amount DESC) AS rank,
  DENSE_RANK() OVER (ORDER BY total_amount DESC) AS dense_rank
FROM orders;
```

### PARTITION BY
```sql
-- Ranking pro Gruppe
SELECT 
  country,
  customer_id,
  total_amount,
  RANK() OVER (PARTITION BY country ORDER BY total_amount DESC) AS rank_in_country
FROM orders;
```

### Running Total
```sql
SELECT 
  order_date,
  total_amount,
  SUM(total_amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

### Moving Average
```sql
SELECT 
  order_date,
  total_amount,
  AVG(total_amount) OVER (
    ORDER BY order_date 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS moving_avg_7days
FROM orders;
```

---

## 📊 Subqueries (Unterabfragen)

### In WHERE Clause
```sql
-- Kunden mit überdurchschnittlichem Umsatz
SELECT * 
FROM customers
WHERE customer_id IN (
  SELECT customer_id 
  FROM orders 
  GROUP BY customer_id 
  HAVING SUM(total_amount) > (SELECT AVG(total_amount) FROM orders)
);
```

### In FROM Clause
```sql
SELECT 
  segment,
  AVG(total) AS avg_per_segment
FROM (
  SELECT 
    customer_id,
    CASE 
      WHEN SUM(total_amount) > 1000 THEN 'High'
      ELSE 'Low'
    END AS segment,
    SUM(total_amount) AS total
  FROM orders
  GROUP BY customer_id
) AS customer_segments
GROUP BY segment;
```

---

## 🛠️ CTEs (Common Table Expressions)

```sql
-- Lesbarere Alternative zu Subqueries
WITH customer_totals AS (
  SELECT 
    customer_id,
    SUM(total_amount) AS total_spent,
    COUNT(*) AS order_count
  FROM orders
  GROUP BY customer_id
)
SELECT 
  customers.name,
  customer_totals.total_spent,
  customer_totals.order_count
FROM customers
JOIN customer_totals 
  ON customers.customer_id = customer_totals.customer_id
WHERE customer_totals.total_spent > 1000;
```

### Mehrere CTEs
```sql
WITH 
high_value_customers AS (
  SELECT customer_id
  FROM orders
  GROUP BY customer_id
  HAVING SUM(total_amount) > 5000
),
recent_orders AS (
  SELECT *
  FROM orders
  WHERE order_date >= '2025-01-01'
)
SELECT 
  ro.order_id,
  ro.customer_id,
  ro.total_amount
FROM recent_orders ro
INNER JOIN high_value_customers hvc
  ON ro.customer_id = hvc.customer_id;
```

---

## 🎯 Häufige Analyse-Pattern

### RFM-Analyse (Recency, Frequency, Monetary)
```sql
WITH customer_metrics AS (
  SELECT 
    customer_id,
    MAX(order_date) AS last_order_date,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_spent
  FROM orders
  GROUP BY customer_id
)
SELECT 
  customer_id,
  DATE_DIFF(CURRENT_DATE(), last_order_date, DAY) AS recency,
  order_count AS frequency,
  total_spent AS monetary,
  CASE 
    WHEN DATE_DIFF(CURRENT_DATE(), last_order_date, DAY) <= 30 
         AND order_count >= 5 
         AND total_spent >= 1000 
    THEN 'VIP'
    WHEN DATE_DIFF(CURRENT_DATE(), last_order_date, DAY) > 365 
    THEN 'At Risk'
    ELSE 'Regular'
  END AS segment
FROM customer_metrics;
```

### Cohort-Analyse
```sql
WITH first_purchase AS (
  SELECT 
    customer_id,
    DATE_TRUNC(MIN(order_date), MONTH) AS cohort_month
  FROM orders
  GROUP BY customer_id
),
customer_orders AS (
  SELECT 
    o.customer_id,
    o.order_date,
    fp.cohort_month,
    DATE_DIFF(
      DATE_TRUNC(o.order_date, MONTH), 
      fp.cohort_month, 
      MONTH
    ) AS months_since_first
  FROM orders o
  JOIN first_purchase fp ON o.customer_id = fp.customer_id
)
SELECT 
  cohort_month,
  months_since_first,
  COUNT(DISTINCT customer_id) AS active_customers
FROM customer_orders
GROUP BY cohort_month, months_since_first
ORDER BY cohort_month, months_since_first;
```

### Top N pro Kategorie
```sql
WITH ranked_products AS (
  SELECT 
    category,
    product_name,
    total_sales,
    RANK() OVER (PARTITION BY category ORDER BY total_sales DESC) AS rank
  FROM product_sales
)
SELECT *
FROM ranked_products
WHERE rank <= 5;
```

---

## ⚠️ Best Practices & Häufige Fehler

### ✅ DO's
```sql
-- Aliase für Klarheit verwenden
SELECT 
  c.name AS customer_name,
  o.total_amount AS order_total
FROM customers AS c
JOIN orders AS o ON c.customer_id = o.customer_id;

-- CTEs für Komplexität
WITH relevant_orders AS (
  -- Klare, wiederverwendbare Logik
)
SELECT * FROM relevant_orders;

-- Kommentare für komplexe Logik
-- Berechne die durchschnittliche Zeit zwischen Bestellungen
SELECT AVG(days_between) FROM order_gaps;
```

### ❌ DON'Ts
```sql
-- SELECT * in Production vermeiden (langsam, verschwendet Ressourcen)
-- ❌ SELECT * FROM large_table;
-- ✅ SELECT id, name, email FROM large_table;

-- Keine impliziten JOINs (schwer lesbar)
-- ❌ SELECT * FROM table1, table2 WHERE table1.id = table2.id;
-- ✅ SELECT * FROM table1 JOIN table2 ON table1.id = table2.id;

-- WHERE vor HAVING verwenden (effizienter)
-- ❌ HAVING country = 'Germany' (wird nach Aggregation gefiltert)
-- ✅ WHERE country = 'Germany' (wird vor Aggregation gefiltert)
```

---

## 🚀 Performance-Tipps

1. **WHERE vor JOIN**: Filter so früh wie möglich
2. **LIMIT verwenden**: Bei Exploration große Datasets begrenzen
3. **Indizes nutzen**: Bei WHERE, JOIN, ORDER BY
4. **EXPLAIN verwenden**: Query-Performance analysieren
5. **Partitionierung**: Bei sehr großen Tabellen (nach Datum)

---

## 📚 Weiterführende Ressourcen

- [BigQuery Standard SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [Window Functions Tutorial](https://mode.com/sql-tutorial/sql-window-functions/)

---

*Aktualisiert: Oktober 2025*