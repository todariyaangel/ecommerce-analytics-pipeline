# End-to-End E-Commerce Data Engineering & Analytics Pipeline

## Project Overview
This repository contains a production-grade, end-to-end data analytics pipeline designed for generic e-commerce transaction validation. The architecture covers the entire data lifecycle: generating behavioral interaction streams, structuring a relational database framework, executing analytical ETL window logic, and running statistical hypothesis validation.

##  Complete Technical Stack
* **Data Ingestion:** Python (Automated conversion funnel and transaction log simulation)
* **Data Warehouse ETL:** PostgreSQL (Relational schema modeling, CTEs, Window Functions)
* **Statistical Computing:** Python (Pandas, NumPy, SciPy for Independent T-Testing)
* **Data Architecture:** Star Schema (Dimension and Fact table separation)
* **Version Control:** Git / GitHub Workspace

##  Execution & Implementation Steps
1. Run the data synthesis script via `python scripts/fetch_data.py` to build raw logs.
2. Load schemas using `scripts/database_etl.sql` inside your relational database engine.
3. Open `scripts/analysis.ipynb` within your environment kernel to compute cohort segments and run variance metrics.

## Key Findings & Statistical Insights
* **Customer Segmentation:** Successfully categorized users into distinct behavioral cohorts based on transaction velocity and monetary thresholds.
* **Hypothesis Testing Results:** An Independent T-Test comparing order values between *Paid Ads* and *Email Marketing* yielded a **P-Value of 0.2045**. 
* **Business Takeaway:** Because the P-Value is greater than 0.05, there is no statistically significant variance in customer spending between these two acquisition channels. Marketing spend can be optimized based on acquisition cost rather than expected individual order sizes.
