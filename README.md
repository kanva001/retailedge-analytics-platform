```markdown
# RetailEdge Analytics Platform  
**Enterprise KPI Validation Framework (Local SQL → AWS Athena)**

## 📌 Overview
RetailEdge Analytics Platform is an end-to-end analytics validation project that demonstrates how enterprise teams **validate business KPIs across systems** after data is migrated from an on-premise database to the cloud.

The project focuses on **reconciling KPIs calculated locally from Microsoft SQL Server** with KPIs produced in **AWS Athena over Parquet data stored in Amazon S3**, highlighting real-world challenges such as schema mismatches, missing dimensions, and key-mapping issues.

---

## 🎯 Business Requirements
- Validate that **cloud analytics KPIs match source system results**
- Detect data loss or transformation errors during ETL
- Ensure KPI trustworthiness for business reporting
- Provide auditable validation results for stakeholders
- Identify model gaps rather than masking discrepancies

---

## 🏗 Architecture (High Level)
```

Microsoft SQL Server (AdventureWorks / Master DB)
↓
Local CSV Exports
↓
Python KPI Calculations
↓
AWS S3 (Parquet Files)
↓
AWS Athena Queries
↓
KPI Validation & Reconciliation

```

---

## 🧰 Tech Stack
**Databases & Storage**
- Microsoft SQL Server (source system, Windows Authentication)
- Amazon S3 (raw & transformed Parquet datasets)

**Analytics & Query**
- AWS Athena
- SQL

**Programming & Validation**
- Python
- pandas
- pyathena

**Cloud**
- AWS (Athena, S3)

**Other**
- Git / GitHub
- CSV & Parquet formats

---

## 📂 Project Structure
```

retailedge-analytics-platform/
├── data/                    # Raw & transformed data
├── etl/                     # ETL scripts
├── local_data/              # Local KPI CSVs from SQL Server
├── scripts/                 # Helper scripts (e.g. ID mapping)
├── unit_tests/              # KPI-specific test scripts (future expansion)
├── results/                 # Validation outputs & summaries
├── sql/                     # SQL reference queries
├── validate_kpis.py         # Main KPI validation runner
├── README.md
└── RetailEdge_Analytics_Project_Summary.pdf

````

---

## 📊 KPIs Validated
| KPI | Status | Notes |
|----|------|------|
| Total Revenue by Month | ❌ FAIL | Aggregation mismatch between systems |
| Top 10 Products | ✅ PASS | Valid after product ID mapping |
| Customer Lifetime Value (CLV) | ❌ FAIL | Differences traced to data scope/modeling |
| Monthly Returns | ⚠️ SKIPPED | Return data not modeled in Athena |
| Revenue by Territory | ⚠️ SKIPPED | Geography dimension missing in Athena |

---

## 🔍 Key Challenges Encountered
- **Business keys vs surrogate keys** (Product Name vs Product ID)
- **Missing dimensions** in Athena fact tables
- **Region mismatches** between Athena and S3 staging buckets
- Schema visibility issues across environments
- Differences caused by **model design**, not ETL failures

---

## ✅ How Issues Were Resolved
- Verified AWS Athena region & S3 staging configuration
- Built sanity checks to confirm Athena connectivity
- Introduced product ID ↔ product name reconciliation
- Explicitly classified failures as:
  - ETL defect
  - Data modeling gap
  - Expected limitation
- Documented skipped KPIs instead of forcing incorrect comparisons

---

## ▶️ How to Run the Validation
```bash
python validate_kpis.py
````

The script will:

* Load local KPI CSVs
* Query AWS Athena
* Compare results
* Output PASS / FAIL / SKIP status
* Save validation summaries to `/results`

---
