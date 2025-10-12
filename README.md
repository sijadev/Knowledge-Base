# 📊 Data Analytics Knowledge Base

> A comprehensive collection of data analytics resources, cheat sheets, and best practices compiled during my Google Data Analytics certification journey.

[![SQL](https://img.shields.io/badge/SQL-BigQuery-blue)](https://cloud.google.com/bigquery)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://www.python.org/)
[![Tableau](https://img.shields.io/badge/Tableau-2024-orange)](https://www.tableau.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 About This Repository

This repository contains my curated notes, cheat sheets, and resources from the **Google Data Analytics Professional Certificate** (2025), enhanced with real-world examples and practical applications. It serves as both a learning journal and a reference guide for data analytics best practices.

## 📚 What's Inside

### 🗂️ **Cheat Sheets**
Quick reference guides for daily work:
- **[SQL Cheat Sheet](data-analytics/5.%20Anhang/Cheat-Sheets/SQL-Cheat-Sheet.md)** - Complete SQL reference with BigQuery specifics
- **[Spreadsheets Cheat Sheet](data-analytics/5.%20Anhang/Cheat-Sheets/Spreadsheets-Cheat-Sheet.md)** - Excel & Google Sheets formulas
- **[Data Visualization](data-analytics/5.%20Anhang/Cheat-Sheets/Data-Visualization-Cheat-Sheet.md)** - Chart selection, dashboard design, color theory

### 🎯 **Practice Exercises**
- **[SQL Exercises](data-analytics/5.%20Anhang/Übungsaufgaben/SQL-Übungen.md)** - 15+ exercises from beginner to advanced with solutions

### 📖 **Reference Materials**
- **[Glossary](data-analytics/5.%20Anhang/Glossar-Erweitert.md)** - 200+ data analytics terms with examples
- **[Best Practices](data-analytics/5.%20Anhang/Best-Practices.md)** - Professional workflows and methodologies
- **[Common Mistakes](data-analytics/5.%20Anhang/Häufige-Fehler.md)** - Learn from typical pitfalls

### 💼 **Real-World Scenarios**
- **[Case Studies](data-analytics/5.%20Anhang/Praxis-Szenarien.md)** - 4 complete analysis scenarios:
  - E-Commerce Conversion Drop Analysis
  - Feature Adoption Analysis
  - Executive Dashboard Design
  - Pricing Optimization

### 📝 **Core Concepts**
Detailed notes on fundamental topics:
- [Data Analysis Process](1.%20Google%20Data%20Analytics/1.0%20Grundlagen/1.1%20Einführung%20in%20die%20Datenanalyse/Datenperspektive%20(Daten%20Analyze%20Prozess%20).md)
- [Analytical Thinking](1.%20Google%20Data%20Analytics/1.0%20Grundlagen/1.1%20Einführung%20in%20die%20Datenanalyse/Analytisches%20Denken.md)
- [Data Analytics Skills](1.%20Google%20Data%20Analytics/1.0%20Grundlagen/1.1%20Einführung%20in%20die%20Datenanalyse/Data%20Analytics%20Fähigkeiten.md)

## 🛠️ Technologies & Tools

**Databases & Query Languages:**
- SQL (BigQuery, PostgreSQL)
- Google Sheets / Excel

**Visualization:**
- Tableau
- Looker Studio
- Excel/Sheets Charts

**Programming:**
- R (planned)
- Python (planned)

**Platforms:**
- Google Cloud Platform
- BigQuery

## 🚀 How to Use This Repository

### For Learning:
1. Start with the [Anhang README](5.%20Anhang/README-Anhang.md) for an overview
2. Use cheat sheets as daily references
3. Practice with SQL exercises
4. Study case studies to see concepts in action

### For Reference:
- Bookmark cheat sheets for quick access
- Use glossary for term lookups
- Reference best practices before projects

### For Interview Prep:
- Review common mistakes
- Study case studies
- Practice SQL exercises

## 📈 Learning Path

### Week 1-2: Foundations
- [ ] SQL Cheat Sheet + Basic exercises
- [ ] Spreadsheets fundamentals
- [ ] Core concepts (Ask, Prepare, Process phases)

### Week 3-4: Intermediate
- [ ] SQL intermediate exercises
- [ ] Best Practices (sections 1-5)
- [ ] Visualization basics

### Week 5-6: Advanced
- [ ] SQL advanced exercises
- [ ] Complete case studies
- [ ] Dashboard design

### Week 7-8: Mastery
- [ ] Real-world project
- [ ] Portfolio piece creation
- [ ] Interview preparation

## 🎓 Certification Progress

- [x] Google Data Analytics Professional Certificate (in progress)
- [ ] Tableau Desktop Specialist
- [ ] Google Cloud Professional Data Engineer

## 💡 Key Learnings

**Top 5 Insights:**
1. **Context is Everything** - Data without business context is just numbers
2. **Correlation ≠ Causation** - Always validate assumptions with experiments
3. **Segment, Segment, Segment** - Aggregated data hides important patterns
4. **Document Everything** - Future you will thank present you
5. **Stakeholder Communication** - Technical accuracy means nothing if not understood

## 📊 Sample Work

Here are examples of analyses and visualizations from this repository:

### SQL Analysis Example
```sql
-- Customer Lifetime Value Calculation with RFM Segmentation
WITH customer_metrics AS (
  SELECT 
    customer_id,
    DATE_DIFF(CURRENT_DATE(), MAX(order_date), DAY) AS recency,
    COUNT(*) AS frequency,
    SUM(total_amount) AS monetary
  FROM orders
  GROUP BY customer_id
)
SELECT 
  customer_id,
  recency,
  frequency,
  monetary,
  CASE 
    WHEN monetary > 1000 AND recency <= 30 THEN 'VIP'
    WHEN frequency > 5 THEN 'Loyal'
    ELSE 'Regular'
  END AS segment
FROM customer_metrics;
```

### Dashboard Design Principles
- **Visual Hierarchy**: Most important metrics at top-left
- **Color Consistency**: Same meaning = same color
- **Progressive Disclosure**: Summary → Details on click
- **Mobile-First**: Responsive design for all devices

## 🤝 Connect With Me

- **LinkedIn:** [Simon Janke](https://linkedin.com/in/your-profile)
- **Portfolio:** [simonjanke.com](https://your-portfolio.com)
- **Email:** your.email@example.com

## 📝 License

This work is licensed under the [MIT License](LICENSE). Feel free to use these resources for your own learning!

## 🙏 Acknowledgments

- Google Data Analytics Professional Certificate program
- Coursera platform
- The data analytics community for inspiration and best practices

---

⭐ **Star this repo** if you find it helpful!  
🔄 **Fork it** to create your own version!  
📧 **Reach out** if you have questions or suggestions!

---

*Last Updated: October 2025*  
*Status: 🚧 Actively maintained and expanded*

## 📌 Quick Links

- [Start Here - Anhang Overview](5.%20Anhang/README-Anhang.md)
- [SQL Cheat Sheet](5.%20Anhang/Cheat-Sheets/SQL-Cheat-Sheet.md)
- [Best Practices](5.%20Anhang/Best-Practices.md)
- [Case Studies](5.%20Anhang/Praxis-Szenarien.md)
