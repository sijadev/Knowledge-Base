---
autor: Simon Janke
title: SQL Übungsaufgaben
type: Übung
date: 2025-10-12
tags:
  - SQL
  - übung
  - praxis
difficulty: Anfänger bis Fortgeschritten
---

# 🎯 SQL Übungsaufgaben mit Lösungen

---

## 📊 Datenbank-Schema

Für alle Übungen verwenden wir folgende Tabellen:

### Tabelle: `customers`
| customer_id | name | email | country | signup_date |
|------------|------|-------|---------|-------------|
| 1 | Anna Schmidt | anna@email.de | Germany | 2024-01-15 |
| 2 | John Doe | john@email.com | USA | 2024-02-20 |
| 3 | Marie Dubois | marie@email.fr | France | 2024-03-10 |
| 4 | Hans Müller | hans@email.de | Germany | 2024-01-25 |
| 5 | Sarah Jones | sarah@email.com | USA | 2024-04-05 |

### Tabelle: `orders`
| order_id | customer_id | order_date | total_amount | status |
|----------|-------------|------------|--------------|---------|
| 101 | 1 | 2024-05-01 | 299.99 | completed |
| 102 | 1 | 2024-06-15 | 149.50 | completed |
| 103 | 2 | 2024-05-10 | 89.99 | completed |
| 104 | 3 | 2024-05-20 | 499.99 | completed |
| 105 | 4 | 2024-06-01 | 199.99 | cancelled |
| 106 | 2 | 2024-07-01 | 299.99 | completed |
| 107 | 1 | 2024-07-15 | 399.99 | completed |

### Tabelle: `products`
| product_id | product_name | category | price | stock |
|-----------|--------------|----------|-------|--------|
| 1 | Laptop Pro | Electronics | 1299.99 | 15 |
| 2 | Wireless Mouse | Accessories | 29.99 | 150 |
| 3 | USB-C Cable | Accessories | 14.99 | 200 |
| 4 | Monitor 27" | Electronics | 349.99 | 25 |
| 5 | Keyboard | Accessories | 79.99 | 80 |

### Tabelle: `order_items`
| order_item_id | order_id | product_id | quantity | price_per_unit |
|--------------|----------|------------|----------|----------------|
| 1 | 101 | 1 | 1 | 1299.99 |
| 2 | 102 | 2 | 3 | 29.99 |
| 3 | 102 | 3 | 2 | 14.99 |
| 4 | 103 | 2 | 1 | 29.99 |
| 5 | 103 | 5 | 1 | 79.99 |
| 6 | 104 | 4 | 1 | 349.99 |
| 7 | 106 | 1 | 1 | 1299.99 |

---

## 🟢 Level 1: Anfänger

### Aufgabe 1.1: Alle Kunden anzeigen
**Aufgabe:** Zeige alle Kundennamen und ihre E-Mail-Adressen an.

<details>
<summary>💡 Hinweis</summary>
Nutze SELECT mit spezifischen Spaltennamen.
</details>

<details>
<summary>✅ Lösung</summary>

```sql
SELECT name, email
FROM customers;
```

**Erwartete Ausgabe:**
```
name            | email
----------------|------------------
Anna Schmidt    | anna@email.de
John Doe        | john@email.com
Marie Dubois    | marie@email.fr
Hans Müller     | hans@email.de
Sarah Jones     | sarah@email.com
```
</details>

---

### Aufgabe 1.2: Deutsche Kunden filtern
**Aufgabe:** Finde alle Kunden aus Deutschland.

<details>
<summary>💡 Hinweis</summary>
Verwende WHERE mit einem Vergleich.
</details>

<details>
<summary>✅ Lösung</summary>

```sql
SELECT *
FROM customers
WHERE country = 'Germany';
```

**Erwartete Ausgabe:** Anna Schmidt und Hans Müller
</details>

---

### Aufgabe 1.3: Bestellungen über 200€
**Aufgabe:** Zeige alle Bestellungen mit einem Gesamtbetrag über 200€.

<details>
<summary>✅ Lösung</summary>

```sql
SELECT order_id, customer_id, total_amount, order_date
FROM orders
WHERE total_amount > 200;
```

**Erwartete Ausgabe:** 4 Bestellungen (101, 104, 106, 107)
</details>

---

### Aufgabe 1.4: Anzahl der Kunden
**Aufgabe:** Wie viele Kunden sind in der Datenbank registriert?

<details>
<summary>💡 Hinweis</summary>
Nutze COUNT().
</details>

<details>
<summary>✅ Lösung</summary>

```sql
SELECT COUNT(*) AS customer_count
FROM customers;
```

**Erwartete Ausgabe:** 5
</details>

---

### Aufgabe 1.5: Durchschnittlicher Bestellwert
**Aufgabe:** Berechne den durchschnittlichen Bestellwert aller abgeschlossenen Bestellungen.

<details>
<summary>✅ Lösung</summary>

```sql
SELECT AVG(total_amount) AS avg_order_value
FROM orders
WHERE status = 'completed';
```

**Erwartete Ausgabe:** ~297.91
</details>

---

## 🟡 Level 2: Mittelstufe

### Aufgabe 2.1: Bestellungen pro Kunde
**Aufgabe:** Zeige für jeden Kunden die Anzahl der Bestellungen und den Gesamtumsatz (nur completed).

<details>
<summary>💡 Hinweis</summary>
Nutze GROUP BY mit COUNT() und SUM().
</details>

<details>
<summary>✅ Lösung</summary>

```sql
SELECT 
  c.customer_id,
  c.name,
  COUNT(o.order_id) AS order_count,
  SUM(o.total_amount) AS total_spent
FROM customers c
LEFT JOIN orders o 
  ON c.customer_id = o.customer_id 
  AND o.status = 'completed'
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC;
```

**Erwartete Ausgabe:**
```
customer_id | name          | order_count | total_spent
------------|---------------|-------------|-------------
1           | Anna Schmidt  | 3           | 849.48
2           | John Doe      | 2           | 389.98
3           | Marie Dubois  | 1           | 499.99
4           | Hans Müller   | 0           | NULL
5           | Sarah Jones   | 0           | NULL
```
</details>

---

### Aufgabe 2.2: Top 3 Produkte nach Umsatz
**Aufgabe:** Finde die 3 meistverkauften Produkte nach Gesamtumsatz.

<details>
<summary>💡 Hinweis</summary>
JOIN order_items und products, nutze SUM() und LIMIT.
</details>

<details>
<summary>✅ Lösung</summary>

```sql
SELECT 
  p.product_name,
  p.category,
  SUM(oi.quantity * oi.price_per_unit) AS total_revenue,
  SUM(oi.quantity) AS total_quantity_sold
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 3;
```

**Erwartete Ausgabe:**
1. Laptop Pro
2. Monitor 27"
3. Wireless Mouse
</details>

---

### Aufgabe 2.3: Monatlicher Umsatz 2024
**Aufgabe:** Berechne den Umsatz pro Monat für das Jahr 2024 (nur completed).

<details>
<summary>💡 Hinweis</summary>
Nutze DATE_TRUNC() oder EXTRACT() mit GROUP BY.
</details>

<details>
<summary>✅ Lösung (BigQuery)</summary>

```sql
SELECT 
  DATE_TRUNC(order_date, MONTH) AS month,
  COUNT(*) AS order_count,
  SUM(total_amount) AS monthly_revenue
FROM orders
WHERE status = 'completed'
  AND EXTRACT(YEAR FROM order_date) = 2024
GROUP BY month
ORDER BY month;
```

**Erwartete Ausgabe:**
```
month      | order_count | monthly_revenue
-----------|-------------|----------------
2024-05-01 | 3           | 889.97
2024-06-01 | 1           | 149.50
2024-07-01 | 2           | 699.98
```
</details>

---

### Aufgabe 2.4: Kunden ohne Bestellungen
**Aufgabe:** Finde alle Kunden, die noch nie eine Bestellung aufgegeben haben.

<details>
<summary>💡 Hinweis</summary>
LEFT JOIN und WHERE order_id IS NULL.
</details>

<details>
<summary>✅ Lösung</summary>

```sql
SELECT 
  c.customer_id,
  c.name,
  c.email,
  c.signup_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

**Erwartete Ausgabe:** Sarah Jones
</details>

---

### Aufgabe 2.5: Produktkategorien Performance
**Aufgabe:** Zeige Umsatz und Anzahl verkaufter Artikel pro Produktkategorie.

<details>
<summary>✅ Lösung</summary>

```sql
SELECT 
  p.category,
  COUNT(DISTINCT oi.order_id) AS order_count,
  SUM(oi.quantity) AS items_sold,
  SUM(oi.quantity * oi.price_per_unit) AS total_revenue,
  ROUND(AVG(oi.price_per_unit), 2) AS avg_price
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
```

**Erwartete Ausgabe:**
```
category     | order_count | items_sold | total_revenue | avg_price
-------------|-------------|------------|---------------|----------
Electronics  | 3           | 3          | 2949.97       | 983.32
Accessories  | 3           | 7          | 139.93        | 24.99
```
</details>

---

## 🔴 Level 3: Fortgeschritten

### Aufgabe 3.1: Customer Lifetime Value (CLV)
**Aufgabe:** Berechne für jeden Kunden:
- Anzahl der Bestellungen
- Gesamtumsatz
- Durchschnittlicher Bestellwert
- Tage seit letzter Bestellung
- Customer Segment (VIP, Regular, Inactive)

**Segmentierungslogik:**
- VIP: Total > 500€ UND letzte Bestellung < 60 Tage
- Regular: Hat Bestellungen, aber kein VIP
- Inactive: Keine Bestellungen

<details>
<summary>💡 Hinweis</summary>
Nutze CTEs, CASE WHEN, DATE_DIFF().
</details>

<details>
<summary>✅ Lösung</summary>

```sql
WITH customer_stats AS (
  SELECT 
    c.customer_id,
    c.name,
    c.country,
    COUNT(o.order_id) AS order_count,
    COALESCE(SUM(CASE WHEN o.status = 'completed' THEN o.total_amount END), 0) AS total_spent,
    COALESCE(AVG(CASE WHEN o.status = 'completed' THEN o.total_amount END), 0) AS avg_order_value,
    MAX(o.order_date) AS last_order_date,
    DATE_DIFF(CURRENT_DATE(), MAX(o.order_date), DAY) AS days_since_last_order
  FROM customers c
  LEFT JOIN orders o ON c.customer_id = o.customer_id
  GROUP BY c.customer_id, c.name, c.country
)
SELECT 
  customer_id,
  name,
  country,
  order_count,
  ROUND(total_spent, 2) AS total_spent,
  ROUND(avg_order_value, 2) AS avg_order_value,
  days_since_last_order,
  CASE 
    WHEN total_spent > 500 AND days_since_last_order <= 60 THEN 'VIP'
    WHEN order_count > 0 THEN 'Regular'
    ELSE 'Inactive'
  END AS customer_segment
FROM customer_stats
ORDER BY total_spent DESC;
```
</details>

---

### Aufgabe 3.2: Cohort-Analyse
**Aufgabe:** Erstelle eine Cohort-Analyse basierend auf dem Signup-Monat. Zeige für jeden Cohort:
- Signup-Monat
- Anzahl der Kunden im Cohort
- Anzahl der Kunden mit mindestens 1 Bestellung
- Conversion Rate
- Durchschnittlicher Umsatz pro Kunde

<details>
<summary>✅ Lösung</summary>

```sql
WITH cohorts AS (
  SELECT 
    DATE_TRUNC(signup_date, MONTH) AS cohort_month,
    customer_id
  FROM customers
),
cohort_stats AS (
  SELECT 
    c.cohort_month,
    COUNT(DISTINCT c.customer_id) AS cohort_size,
    COUNT(DISTINCT o.customer_id) AS customers_with_orders,
    SUM(CASE WHEN o.status = 'completed' THEN o.total_amount ELSE 0 END) AS total_revenue
  FROM cohorts c
  LEFT JOIN orders o ON c.customer_id = o.customer_id
  GROUP BY c.cohort_month
)
SELECT 
  cohort_month,
  cohort_size,
  customers_with_orders,
  ROUND(customers_with_orders * 100.0 / cohort_size, 2) AS conversion_rate_percent,
  ROUND(total_revenue / cohort_size, 2) AS avg_revenue_per_customer
FROM cohort_stats
ORDER BY cohort_month;
```

**Erwartete Ausgabe:**
```
cohort_month | cohort_size | customers_with_orders | conversion_rate | avg_revenue
-------------|-------------|----------------------|-----------------|-------------
2024-01-01   | 2           | 1                    | 50.00           | 424.74
2024-02-01   | 1           | 1                    | 100.00          | 389.98
2024-03-01   | 1           | 1                    | 100.00          | 499.99
2024-04-01   | 1           | 0                    | 0.00            | 0.00
```
</details>

---

### Aufgabe 3.3: Produkt-Affinität (Warenkorbanalyse)
**Aufgabe:** Finde Produkte, die oft zusammen gekauft werden. Zeige für jedes Produktpaar:
- Produkt A
- Produkt B
- Wie oft wurden sie zusammen bestellt
- Sortiert nach Häufigkeit

<details>
<summary>💡 Hinweis</summary>
Self-JOIN auf order_items.
</details>

<details>
<summary>✅ Lösung</summary>

```sql
SELECT 
  p1.product_name AS product_a,
  p2.product_name AS product_b,
  COUNT(*) AS times_bought_together
FROM order_items oi1
INNER JOIN order_items oi2 
  ON oi1.order_id = oi2.order_id 
  AND oi1.product_id < oi2.product_id  -- Vermeidet Duplikate
INNER JOIN products p1 ON oi1.product_id = p1.product_id
INNER JOIN products p2 ON oi2.product_id = p2.product_id
GROUP BY p1.product_name, p2.product_name
HAVING COUNT(*) > 1  -- Nur wenn mindestens 2x zusammen gekauft
ORDER BY times_bought_together DESC;
```
</details>

---

### Aufgabe 3.4: RFM-Analyse (Recency, Frequency, Monetary)
**Aufgabe:** Erstelle eine RFM-Segmentierung der Kunden:
- **Recency**: Tage seit letzter Bestellung
- **Frequency**: Anzahl der Bestellungen
- **Monetary**: Gesamtumsatz

Vergib für jede Dimension einen Score von 1-5 (5 = am besten).

<details>
<summary>✅ Lösung</summary>

```sql
WITH customer_rfm AS (
  SELECT 
    c.customer_id,
    c.name,
    DATE_DIFF(CURRENT_DATE(), MAX(o.order_date), DAY) AS recency,
    COUNT(o.order_id) AS frequency,
    SUM(CASE WHEN o.status = 'completed' THEN o.total_amount ELSE 0 END) AS monetary
  FROM customers c
  LEFT JOIN orders o ON c.customer_id = o.customer_id
  GROUP BY c.customer_id, c.name
),
rfm_scored AS (
  SELECT 
    *,
    CASE 
      WHEN recency IS NULL THEN 1
      WHEN recency <= 30 THEN 5
      WHEN recency <= 60 THEN 4
      WHEN recency <= 90 THEN 3
      WHEN recency <= 180 THEN 2
      ELSE 1
    END AS r_score,
    CASE 
      WHEN frequency >= 4 THEN 5
      WHEN frequency >= 3 THEN 4
      WHEN frequency >= 2 THEN 3
      WHEN frequency >= 1 THEN 2
      ELSE 1
    END AS f_score,
    CASE 
      WHEN monetary >= 800 THEN 5
      WHEN monetary >= 500 THEN 4
      WHEN monetary >= 300 THEN 3
      WHEN monetary >= 100 THEN 2
      WHEN monetary > 0 THEN 1
      ELSE 0
    END AS m_score
  FROM customer_rfm
)
SELECT 
  customer_id,
  name,
  recency,
  frequency,
  ROUND(monetary, 2) AS monetary,
  r_score,
  f_score,
  m_score,
  (r_score + f_score + m_score) AS rfm_total_score,
  CASE 
    WHEN (r_score + f_score + m_score) >= 12 THEN 'Champions'
    WHEN (r_score + f_score + m_score) >= 9 THEN 'Loyal Customers'
    WHEN (r_score + f_score + m_score) >= 6 THEN 'Potential Loyalists'
    WHEN (r_score + f_score + m_score) >= 3 THEN 'At Risk'
    ELSE 'Lost'
  END AS customer_segment
FROM rfm_scored
ORDER BY rfm_total_score DESC;
```
</details>

---

### Aufgabe 3.5: Window Functions - Running Total
**Aufgabe:** Zeige für jeden Tag:
- Das Datum
- Tagesumsatz
- Kumulativer Umsatz (Running Total)
- 7-Tage gleitender Durchschnitt

<details>
<summary>✅ Lösung</summary>

```sql
WITH daily_revenue AS (
  SELECT 
    order_date,
    SUM(total_amount) AS daily_revenue
  FROM orders
  WHERE status = 'completed'
  GROUP BY order_date
)
SELECT 
  order_date,
  ROUND(daily_revenue, 2) AS daily_revenue,
  ROUND(SUM(daily_revenue) OVER (ORDER BY order_date), 2) AS running_total,
  ROUND(AVG(daily_revenue) OVER (
    ORDER BY order_date 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ), 2) AS moving_avg_7days
FROM daily_revenue
ORDER BY order_date;
```
</details>

---

## 🎯 Bonus-Challenge: Komplexe Business-Frage

### Challenge: Customer Retention Report
**Aufgabe:** Erstelle einen umfassenden Report, der folgendes zeigt:

1. Für jeden Monat in 2024:
   - Anzahl neuer Kunden (Signup im Monat)
   - Anzahl aktiver Kunden (mindestens 1 Bestellung im Monat)
   - Anzahl wiederkehrender Kunden (hatte bereits vorher bestellt)
   - Retention Rate (Wiederkehrende / Aktive aus Vormonat)
   - Monatsumsatz
   - MRR (Monthly Recurring Revenue) pro Kunde

2. Zusätzlich:
   - Churn Rate (Kunden die im Vormonat aktiv waren, jetzt nicht)
   - Customer Acquisition Cost Potential (wenn angenommen: Marketing Budget / Neue Kunden)

<details>
<summary>💡 Hinweis</summary>
Diese Aufgabe erfordert mehrere CTEs und Window Functions. Schritt für Schritt:
1. Monatliche Neukunden
2. Monatliche aktive Kunden
3. Wiederkehrende Kunden identifizieren
4. Alles zusammenführen
</details>

<details>
<summary>✅ Lösung</summary>

```sql
WITH monthly_signups AS (
  SELECT 
    DATE_TRUNC(signup_date, MONTH) AS month,
    COUNT(*) AS new_customers
  FROM customers
  GROUP BY month
),
monthly_active_customers AS (
  SELECT 
    DATE_TRUNC(order_date, MONTH) AS month,
    COUNT(DISTINCT customer_id) AS active_customers,
    SUM(CASE WHEN status = 'completed' THEN total_amount ELSE 0 END) AS monthly_revenue
  FROM orders
  GROUP BY month
),
customer_first_order AS (
  SELECT 
    customer_id,
    MIN(order_date) AS first_order_date
  FROM orders
  GROUP BY customer_id
),
monthly_returning AS (
  SELECT 
    DATE_TRUNC(o.order_date, MONTH) AS month,
    COUNT(DISTINCT o.customer_id) AS returning_customers
  FROM orders o
  INNER JOIN customer_first_order cfo 
    ON o.customer_id = cfo.customer_id
  WHERE DATE_TRUNC(o.order_date, MONTH) > DATE_TRUNC(cfo.first_order_date, MONTH)
  GROUP BY month
),
combined AS (
  SELECT 
    COALESCE(ms.month, mac.month, mr.month) AS month,
    COALESCE(ms.new_customers, 0) AS new_customers,
    COALESCE(mac.active_customers, 0) AS active_customers,
    COALESCE(mr.returning_customers, 0) AS returning_customers,
    COALESCE(mac.monthly_revenue, 0) AS monthly_revenue
  FROM monthly_signups ms
  FULL OUTER JOIN monthly_active_customers mac ON ms.month = mac.month
  FULL OUTER JOIN monthly_returning mr ON ms.month = mr.month
)
SELECT 
  month,
  new_customers,
  active_customers,
  returning_customers,
  ROUND(monthly_revenue, 2) AS monthly_revenue,
  ROUND(monthly_revenue / NULLIF(active_customers, 0), 2) AS revenue_per_customer,
  ROUND(returning_customers * 100.0 / NULLIF(active_customers, 0), 2) AS returning_rate_percent,
  LAG(active_customers) OVER (ORDER BY month) AS prev_month_active,
  ROUND(
    (LAG(active_customers) OVER (ORDER BY month) - active_customers) * 100.0 / 
    NULLIF(LAG(active_customers) OVER (ORDER BY month), 0),
    2
  ) AS churn_rate_percent
FROM combined
ORDER BY month;
```
</details>

---

## 📚 Weiterführende Übungen

Für weitere Praxis empfehlen wir:
- [LeetCode SQL Problems](https://leetcode.com/problemset/database/)
- [HackerRank SQL](https://www.hackerrank.com/domains/sql)
- [SQLZoo](https://sqlzoo.net/)
- [Mode SQL Tutorial](https://mode.com/sql-tutorial/)

---

*Erstellt: Oktober 2025*