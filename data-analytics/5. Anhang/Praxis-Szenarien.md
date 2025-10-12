---
autor: Simon Janke
title: Praktische Analyse-Szenarien
type: Ressource
date: 2025-10-12
tags:
  - praxis
  - case-studies
  - real-world
  - szenarien
---

# 🎯 Praktische Analyse-Szenarien - Von der Frage zur Lösung

Real-world Szenarien mit Schritt-für-Schritt-Lösungen.

---

## 📦 Szenario 1: E-Commerce Conversion-Drop

### Die Situation
```
Du arbeitest für einen Online-Shop.
Dein Manager kommt zu dir: "Die Conversion-Rate ist um 15% gefallen. 
Finde heraus warum und was wir tun können!"
```

### Schritt 1: Problem spezifizieren (ASK)

**Klärende Fragen:**
```
✓ Seit wann ist der Drop?
  → "Seit 2 Wochen"
  
✓ Für alle User oder Segmente?
  → "Gute Frage, weiß ich nicht"
  
✓ Alle Produkte oder spezifisch?
  → "Alle soweit ich weiß"
  
✓ Gab es Änderungen an der Website?
  → "Ja, neues Checkout-Design vor 3 Wochen"
  
✓ Was ist die aktuelle Conversion-Rate?
  → "2.1% (war 2.47%)"
```

**SMART Frage formulieren:**
```
"Identifiziere die Hauptursachen für den 15% Conversion-Drop 
seit dem neuen Checkout-Rollout vor 3 Wochen und empfehle 
Maßnahmen zur Wiederherstellung der baseline Conversion von 2.47%"
```

### Schritt 2: Daten vorbereiten (PREPARE)

**Benötigte Daten:**
```sql
-- Web Analytics
SELECT 
  date,
  device_type,
  product_category,
  checkout_step,
  COUNT(DISTINCT session_id) AS sessions,
  COUNT(DISTINCT CASE WHEN purchased = TRUE THEN session_id END) AS conversions
FROM analytics_events
WHERE date >= DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY)
GROUP BY 1, 2, 3, 4;

-- A/B Test Data (Checkout Versionen)
SELECT 
  user_id,
  checkout_version, -- 'old' vs 'new'
  device_type,
  completed_purchase
FROM checkout_experiments
WHERE test_start_date >= '2025-09-01';
```

### Schritt 3: Explorieren & Analysieren (PROCESS & ANALYZE)

**Hypothesen testen:**

**Hypothese 1: Geräte-spezifisch?**
```sql
WITH conversion_by_device AS (
  SELECT 
    DATE_TRUNC('week', date) AS week,
    device_type,
    AVG(CASE WHEN purchased THEN 1.0 ELSE 0.0 END) AS conversion_rate
  FROM sessions
  WHERE date >= DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY)
  GROUP BY 1, 2
)
SELECT * FROM conversion_by_device
ORDER BY week, device_type;
```

**Ergebnis:**
```
week       | device_type | conversion_rate
2025-08-20 | Mobile      | 0.0189
2025-08-20 | Desktop     | 0.0312
2025-08-20 | Tablet      | 0.0267
----- NEW CHECKOUT ROLLOUT -----
2025-09-10 | Mobile      | 0.0095  ← DROP!
2025-09-10 | Desktop     | 0.0305  ← OK
2025-09-10 | Tablet      | 0.0261  ← OK
```

**💡 Insight:** Problem ist Mobile-spezifisch!

**Hypothese 2: Wo im Funnel brechen User ab?**
```sql
SELECT 
  checkout_step,
  device_type,
  COUNT(*) AS users,
  COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY device_type) AS pct
FROM checkout_funnel
WHERE date >= '2025-09-10'
GROUP BY 1, 2
ORDER BY 2, 1;
```

**Ergebnis:**
```
Mobile Funnel:
Step 1 (Cart)     : 10000 users (100%)
Step 2 (Login)    : 8500 users (85%)
Step 3 (Address)  : 7200 users (72%)
Step 4 (Payment)  : 2800 users (28%) ← MASSIVE DROP!
Step 5 (Confirm)  : 2650 users (27%)
```

**💡 Insight:** Mobile User brechen bei Payment ab!

**Hypothese 3: Was ist anders am neuen Payment-Screen?**
```
Qualitative Analyse:
- Screenshot Comparison old vs new
- User Testing Videos
- Customer Support Tickets

Findings:
- Payment-Button ist auf Mobile "below the fold"
- User scrollen nicht, denken Seite ist broken
- Support-Tickets: "Kann nicht bezahlen"
```

### Schritt 4: Visualisieren (SHARE)

**Dashboard erstellen:**

```
┌─────────────────────────────────────────┐
│ Conversion Drop Analysis                │
├─────────────────────────────────────────┤
│                                         │
│ Key Finding: Mobile-Payment-Step Issue  │
│                                         │
│ [Line Chart: Conversion over Time]     │
│  - Desktop: stable                      │
│  - Mobile: dropped at rollout          │
│                                         │
│ [Funnel Chart: Mobile Checkout]        │
│  Cart → Login → Address → PAYMENT ⚠️   │
│   100%   85%     72%       28%         │
│                                         │
│ [Heatmap: Mobile Payment Page]         │
│  - Button not visible without scroll    │
│                                         │
└─────────────────────────────────────────┘
```

### Schritt 5: Handeln (ACT)

**Empfehlungen:**

**Quick Win (1 Tag):**
```
✓ Move Payment-Button above fold on Mobile
✓ Estimated Impact: +50% recovery (1.2% → 1.8% CR)
✓ Implementation: CSS change only
```

**Short-term (1 Week):**
```
✓ Add progress indicator
✓ Improve mobile form UX
✓ Add "Scroll down to continue" hint
✓ Estimated Impact: +30% additional (+0.3%)
```

**Long-term (1 Month):**
```
✓ Redesign mobile checkout (one-page)
✓ Apple Pay / Google Pay integration
✓ A/B test optimizations
✓ Target: 3.0% CR (20% above baseline)
```

**Action Plan:**
```
Day 1: CSS Hotfix deployed
Day 2-7: Monitor results, iterate
Week 2: Start short-term improvements
Week 4: Plan long-term redesign
```

**Success Metrics:**
```
Primary: Mobile Conversion Rate
Target: 2.47% within 2 weeks

Counter-Metrics:
- Desktop CR (should not decrease)
- Payment Error Rate
- Page Load Time

Guardrails:
- Revenue per Session
- Customer Satisfaction (CSAT)
```

---

## 📱 Szenario 2: Feature Adoption niedrig

### Die Situation
```
Product Manager: "Wir haben ein neues Feature gelauncht vor 1 Monat,
aber nur 5% der User nutzen es. Sollten wir es entfernen? 
Was läuft schief?"
```

### Analyse-Schritte

**1. Feature verstehen:**
```
Was: Social Sharing Feature
Wo: Nach Kauf auf Thank-You-Page
Wer: Alle User sehen es
Ziel: Viral Growth
```

**2. Adoption-Metriken definieren:**
```sql
WITH feature_exposure AS (
  SELECT 
    user_id,
    MIN(event_timestamp) AS first_exposure,
    COUNTIF(event_type = 'feature_viewed') AS views,
    COUNTIF(event_type = 'feature_used') AS uses
  FROM events
  WHERE event_timestamp >= '2025-09-01'
    AND (event_type = 'feature_viewed' OR event_type = 'feature_used')
  GROUP BY user_id
)
SELECT 
  COUNT(DISTINCT user_id) AS exposed_users,
  COUNT(DISTINCT CASE WHEN uses > 0 THEN user_id END) AS adopted_users,
  COUNT(DISTINCT CASE WHEN uses > 0 THEN user_id END) * 100.0 / 
    COUNT(DISTINCT user_id) AS adoption_rate,
  AVG(uses) AS avg_uses_per_user
FROM feature_exposure;
```

**Ergebnis:**
```
exposed_users: 10,000
adopted_users: 500
adoption_rate: 5%
avg_uses_per_user: 0.08
```

**3. Hypothesen generieren:**
```
H1: User sehen das Feature nicht (Visibility)
H2: User verstehen nicht was es macht (Clarity)
H3: User sehen keinen Wert (Value Prop)
H4: Feature ist zu kompliziert (Friction)
H5: Wrong target audience (Product-Market Fit)
```

**4. Hypothesen testen:**

**H1: Visibility**
```sql
-- Wie viele User scrollen zur Position des Features?
SELECT 
  AVG(CASE WHEN max_scroll_depth > feature_position THEN 1 ELSE 0 END) AS visibility_rate
FROM page_analytics
WHERE page_type = 'thank_you';

Result: 98% visibility → Not the issue
```

**H2: Clarity (Qualitative)**
```
User Interviews (n=20):
- 15/20: "Ich hab's gesehen, aber nicht verstanden"
- 10/20: "Warum sollte ich das teilen?"
- 5/20: "Ich hab's versucht, aber nicht funktioniert"

→ Clarity + Value Prop Problem!
```

**H3: Value Prop Test**
```
A/B Test:
Variant A: "Share your purchase" (Current)
Variant B: "Get 10% off next order by sharing"

Result after 1 week:
A: 5% adoption
B: 23% adoption

→ Incentive dramatically increases adoption!
```

**5. Segmentierung:**
```sql
-- Welche User adopten das Feature?
SELECT 
  customer_segment,
  product_category,
  COUNT(*) AS users,
  AVG(CASE WHEN feature_used THEN 1 ELSE 0 END) AS adoption_rate
FROM users_with_feature
GROUP BY 1, 2
ORDER BY 4 DESC;
```

**Ergebnis:**
```
Young users (18-25): 12% adoption
Fashion category: 15% adoption
Tech products: 2% adoption

→ Feature resonates mit jungen Fashion-Käufern!
```

**6. Empfehlungen:**

**Immediate:**
```
✓ Add incentive ("10% off next order")
✓ Target Fashion category first
✓ Improve copy and value prop
```

**Short-term:**
```
✓ A/B test different incentives
✓ Add social proof ("1000 people shared today")
✓ Simplify sharing flow
```

**Long-term:**
```
✓ Personalized incentives by segment
✓ Referral tracking and attribution
✓ Expand to other touchpoints (email, app)
```

---

## 📊 Szenario 3: Dashboard Anfrage

### Die Situation
```
CEO: "Ich brauche ein Dashboard um die Gesundheit des Business 
auf einen Blick zu sehen. Was sind die wichtigsten Metriken?"
```

### Analyse-Vorgehen

**1. Stakeholder Interview:**
```
Fragen:
✓ Was sind deine Top 3 Business-Prioritäten?
  → "Growth, Profitability, Customer Satisfaction"
  
✓ Wie oft würdest du das Dashboard ansehen?
  → "Täglich morgens"
  
✓ Welche Entscheidungen triffst du basierend darauf?
  → "Budget-Allocation, Team-Priorities, Investor-Updates"
  
✓ Mobile oder Desktop?
  → "Primär Desktop, manchmal Mobile"
```

**2. Metriken-Hierarchie definieren:**

**North Star Metrics (Top Level):**
```
1. Monthly Recurring Revenue (MRR)
   - Why: Direkt tied to Business Wachstum
   
2. Customer Lifetime Value (CLV)
   - Why: Langfristige Profitabilität
   
3. Net Promoter Score (NPS)
   - Why: Customer Satisfaction
```

**Supporting Metrics (Second Level):**
```
Revenue:
- New MRR (from new customers)
- Expansion MRR (upsells)
- Churn MRR (lost)

Customers:
- New Customers
- Churn Rate
- Retention Rate

Efficiency:
- CAC (Customer Acquisition Cost)
- LTV/CAC Ratio
- Burn Rate
```

**3. Dashboard-Design:**

```
┌─────────────────────────────────────────────────────────────┐
│ Executive Dashboard                          Last Updated: Now │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                │
│  │   MRR    │  │   CLV    │  │   NPS    │                │
│  │  $1.2M   │  │  $5,400  │  │    52    │                │
│  │ ↑ 15% MoM│  │ ↑ 8% MoM │  │  ↓ 2pts  │                │
│  │          │  │          │  │  ⚠️       │                │
│  └──────────┘  └──────────┘  └──────────┘                │
│                                                             │
│  Revenue Breakdown                  Customer Metrics        │
│  ┌────────────────────┐             ┌──────────────────┐  │
│  │                    │             │                  │  │
│  │ [Waterfall Chart]  │             │ [Line Chart]     │  │
│  │ MRR Components     │             │ Churn & Retention│  │
│  │                    │             │                  │  │
│  └────────────────────┘             └──────────────────┘  │
│                                                             │
│  Efficiency Metrics                                         │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ CAC: $850  │ LTV/CAC: 6.4x │ Burn Rate: $200k/mo   │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                             │
│  [Filters: Date Range | Segment | Region]                  │
└─────────────────────────────────────────────────────────────┘
```

**4. SQL für Metriken:**

```sql
-- MRR Calculation
WITH monthly_revenue AS (
  SELECT 
    DATE_TRUNC('month', date) AS month,
    SUM(CASE WHEN subscription_type = 'new' THEN amount END) AS new_mrr,
    SUM(CASE WHEN subscription_type = 'expansion' THEN amount END) AS expansion_mrr,
    SUM(CASE WHEN subscription_type = 'churn' THEN -amount END) AS churn_mrr
  FROM subscriptions
  WHERE date >= DATE_SUB(CURRENT_DATE(), INTERVAL 12 MONTH)
  GROUP BY 1
)
SELECT 
  month,
  new_mrr + expansion_mrr - churn_mrr AS net_new_mrr,
  SUM(net_new_mrr) OVER (ORDER BY month) AS cumulative_mrr
FROM monthly_revenue
ORDER BY month;
```

**5. Automatisierung:**
```
✓ Scheduled refresh: Every hour
✓ Email digest: Daily 7am
✓ Alerts: When MRR < Target oder Churn > 5%
✓ Mobile-optimized version
```

---

## 🎯 Szenario 4: Pricing Optimization

### Die Situation
```
Product Manager: "Sollten wir unseren Preis von $99 auf $129 erhöhen?
Wie viele Kunden würden wir verlieren und lohnt es sich?"
```

### Analyse-Ansatz

**1. Elastizitäts-Analyse:**
```sql
-- Historische Preisänderungen analysieren
WITH price_changes AS (
  SELECT 
    change_date,
    old_price,
    new_price,
    (new_price - old_price) * 100.0 / old_price AS price_change_pct
  FROM pricing_history
),
conversion_impact AS (
  SELECT 
    pc.change_date,
    pc.price_change_pct,
    AVG(CASE WHEN date BETWEEN pc.change_date - 30 AND pc.change_date - 1 
        THEN conversion_rate END) AS pre_change_conversion,
    AVG(CASE WHEN date BETWEEN pc.change_date AND pc.change_date + 30 
        THEN conversion_rate END) AS post_change_conversion
  FROM price_changes pc
  JOIN daily_metrics dm ON dm.date BETWEEN pc.change_date - 30 AND pc.change_date + 30
  GROUP BY 1, 2
)
SELECT 
  AVG(price_change_pct) AS avg_price_increase,
  AVG((post_change_conversion - pre_change_conversion) / pre_change_conversion * 100) 
    AS avg_conversion_impact
FROM conversion_impact;
```

**2. Price Sensitivity Segmente:**
```sql
SELECT 
  customer_segment,
  COUNT(*) AS customers,
  AVG(purchases_per_year) AS avg_purchases,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY willingness_to_pay) AS median_wtp
FROM customer_survey
GROUP BY 1;
```

**3. Revenue Simulation:**
```python
# Python für Simulation
current_price = 99
new_price = 129
current_customers = 1000
estimated_elasticity = -1.5  # -1.5% demand per 1% price increase

price_increase_pct = (new_price - current_price) / current_price
demand_change = estimated_elasticity * price_increase_pct
new_customers = current_customers * (1 + demand_change)

current_revenue = current_price * current_customers
new_revenue = new_price * new_customers

print(f"Current Revenue: ${current_revenue:,.0f}")
print(f"New Revenue: ${new_revenue:,.0f}")
print(f"Change: {(new_revenue - current_revenue) / current_revenue * 100:.1f}%")
print(f"Customer Loss: {current_customers - new_customers:.0f} (-{(1 - new_customers/current_customers) * 100:.1f}%)")
```

**4. Empfehlung:**
```
Scenario Analysis:

Scenario 1: Aggressive ($129)
- Customer Loss: -35%
- Revenue Impact: -16%
❌ NOT RECOMMENDED

Scenario 2: Moderate ($109)  
- Customer Loss: -12%
- Revenue Impact: +3%
✅ RECOMMENDED

Scenario 3: Gradual
- Phase 1: $109 (now)
- Phase 2: $119 (in 6 months)
- Phase 3: $129 (in 12 months)
✅✅ BEST APPROACH

Implementation:
- Grandfather existing customers at $99
- New customers pay $109
- Communicate value, not just price
- Monitor closely for first 30 days
```

---

## 📚 Allgemeine Lessons Learned

### Von Problemen zu Lösungen

**Pattern:**
```
1. ASK: Problem spezifizieren, Kontext verstehen
2. PREPARE: Daten identifizieren und sammeln
3. PROCESS: Daten bereinigen und validieren
4. ANALYZE: Hypothesen bilden und testen, segmentieren
5. SHARE: Visualisieren und Story erzählen
6. ACT: Priorisierte Empfehlungen mit Impact/Effort
```

### Erfolgs-Faktoren

```
✓ Stakeholder früh einbinden
✓ Hypothesen-getrieben vorgehen
✓ Segmentieren, segmentieren, segmentieren
✓ Qualitativ + Quantitativ kombinieren
✓ Quick Wins identifizieren
✓ Impact quantifizieren
✓ Follow-up Plan definieren
```

---

*Aktualisiert: Oktober 2025*