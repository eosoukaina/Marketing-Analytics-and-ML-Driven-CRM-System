# 📊 Marketing Analytics & ML-Driven CRM System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Analytics-336791?logo=postgresql)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?logo=scikit-learn)
![ETL](https://img.shields.io/badge/ETL-Pipeline-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

**End-to-end data engineering project** combining marketing analytics, automated CRM workflows, ETL pipelines, and machine learning for customer conversion prediction.

> 📚 **Academic Project**: Travail Pratique - Data Engineering & Analytics  
> 👩‍🏫 **Supervised by**: Prof. Hind Abidi  
> 🎓 **Institution**: École Nationale des Sciences Appliquées (ENSA)  
> 🗓️ **Completed**: December 2025

---

## 🎯 Project Overview

This project demonstrates comprehensive **data engineering skills** through a real-world marketing analytics scenario. It encompasses the full data lifecycle: from data generation and API integration to ETL pipeline development, SQL analytics, and ML model deployment.

### **Key Technical Achievements**
- ✅ Built production-ready **ETL pipeline** (Extract-Transform-Load)
- ✅ Developed **ML models** achieving 78% accuracy for conversion prediction
- ✅ Implemented **automated email workflows** using Brevo API
- ✅ Designed **PostgreSQL analytics schema** with advanced SQL queries
- ✅ Created comprehensive **data visualizations** for business insights

---

## 📋 Project Deliverables

### **✅ Part 1 - Marketing Automation & Social Media Analytics**
| Deliverable | Status | Files |
|-------------|--------|-------|
| Email automation script (Brevo API) | ✅ Completed | `partie1/src/email_automation.py` |
| Social media analysis notebook | ✅ Completed | `partie1/notebooks/social_media_analysis.ipynb` |
| Visualizations (9 charts) | ✅ Completed | `partie1/outputs/social_analysis/` |
| CSV datasets (15 subscribers + 30 posts) | ✅ Completed | `partie1/data/*.csv` |

### **✅ Part 2 - Data Engineering & Machine Learning Pipeline**
| Deliverable | Status | Files |
|-------------|--------|-------|
| PostgreSQL schema + 4 SQL queries | ✅ Completed | `partie2/sql/analytics_queries.sql` |
| ETL Pipeline (Extract-Transform-Load) | ✅ Completed | `partie2/scripts/etl_pipeline.py` |
| ML dataset generation (1000 users) | ✅ Completed | `partie2/scripts/generate_ml_data.py` |
| ML notebook (2 models) | ✅ Completed | `partie2/notebooks/ml_conversion_prediction.ipynb` |
| PostgreSQL connection tests | ✅ Completed | Tests validated |

### **📊 Key Performance Metrics**
- **Marketing Analytics**: 15 emails sent, 30 social posts analyzed, 5.89% avg engagement rate
- **ML Models**: 1000-user dataset, **78% accuracy** (Random Forest), AUC-ROC 0.85
- **Data Pipeline**: ETL execution time **0.15s** (optimized), 2923 visits processed
- **SQL Analytics**: 4 production-ready queries (conversion rates, ARPU, cohort analysis)

---

## 🗂️ Project Structure

```
marketing-analytics-ml-crm/
├── partie1/                          # Marketing Automation & Analytics
│   ├── src/
│   │   └── email_automation.py       # Automated emails with Brevo API
│   ├── notebooks/
│   │   └── social_media_analysis.ipynb  # Social media analysis
│   ├── data/
│   │   ├── inscrits.csv              # Email database (15 subscribers)
│   │   ├── social_posts.csv          # Social media posts (30 posts)
│   │   └── email_results.json        # Email delivery results
│   └── outputs/
│       └── social_analysis/          # Charts and reports
│
├── partie2/                          # Data Engineering & ML Pipeline
│   ├── sql/
│   │   └── analytics_queries.sql     # Schema + 4 analytics queries
│   ├── scripts/
│   │   ├── generate_ml_data.py       # ML dataset generation (1000 users)
│   │   └── etl_pipeline.py           # ETL Pipeline (Matomo → PostgreSQL)
│   ├── notebooks/
│   │   └── ml_conversion_prediction.ipynb  # ML: Logistic + Random Forest
│   └── data/
│       └── user_behavior.csv         # ML dataset (11 features)
│
├── .env.example                      # API configuration template
├── .gitignore                        # Git exclusions
├── requirements.txt                  # Python dependencies
└── README.md                         # Documentation (this file)
```

---

## 🎓 Technical Objectives & Skills Demonstrated

### **Data Engineering**
- ✅ Designed and implemented **ETL pipeline** (Matomo API → PostgreSQL)
- ✅ Built **scalable database schema** for marketing analytics
- ✅ Developed **SQL queries** for business intelligence (conversion rates, ARPU, cohort analysis)
- ✅ Generated realistic datasets (1000+ users with 11 features)

### **Machine Learning & Analytics**
- ✅ Trained and compared **ML models** (Logistic Regression vs Random Forest)
- ✅ Performed **feature engineering** and importance analysis
- ✅ Implemented **model evaluation** (ROC-AUC, confusion matrices, cross-validation)
- ✅ Created **data visualizations** for social media performance analysis

### **API Integration & Automation**
- ✅ Integrated **Brevo API** for automated email campaigns
- ✅ Implemented **error handling** and logging mechanisms
- ✅ Managed **environment variables** and secure API key storage

---

## 🛠️ Installation

### **Prerequisites**
- Python 3.11+
- PostgreSQL 13+ ([Download here](https://www.postgresql.org/download/))
- Brevo account ([Free registration](https://www.brevo.com/))
- Git

### **1. Clone the repository**
```bash
git clone https://github.com/eosoukaina/Marketing-Analytics-and-ML-Driven-CRM-System.git
cd Marketing-Analytics-and-ML-Driven-CRM-System
```

### **2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# OR
source .venv/bin/activate   # Linux/Mac
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure environment variables**

**For Part 1 (Marketing Automation):** Create `.env` at root:
```env
BREVO_API_KEY=your_brevo_api_key
SENDER_EMAIL=hello@startup.com
SENDER_NAME=Startup Team
```

**For Part 2 (Data Pipeline):** Create `partie2/.env`:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=marketing_db
DB_USER=postgres
DB_PASSWORD=your_password
MATOMO_API_URL=https://your-instance.matomo.cloud/
```

⚠️ **Note**: `.env.example` templates are provided in each folder.

---

## 🚀 Usage Guide

### **Part 1: Marketing Automation & Analytics**

#### **1. Email Automation**
```bash
cd partie1/src
python email_automation.py
```
**Output**: 15 personalized emails sent + JSON logs in `data/email_results.json`

#### **2. Social Media Analytics**
```bash
cd partie1/notebooks
jupyter notebook social_media_analysis.ipynb
```
**Output**:
- 📊 9 visualizations (platform engagement, likes distribution, temporal heatmaps)
- 📈 Statistics: Average engagement rate = **5.89%**
- 🎯 Best performing platform: **Facebook** (7.2% engagement)

---

### **Part 2: Data Engineering & ML Pipeline**

#### **1. Database Setup**
```bash
# Create database
psql -U postgres -c "CREATE DATABASE marketing_db;"

# Load schema and test data
psql -U postgres -d marketing_db -f partie2/sql/analytics_queries.sql
```
**Output**: Tables `events` and `sessions` created + test data inserted

#### **2. Generate ML Dataset**
```bash
cd partie2/scripts
python generate_ml_data.py
```
**Output**: `user_behavior.csv` file with **1000 users** and **11 features**

#### **3. Run ETL Pipeline**
```bash
python etl_pipeline.py
```
**Output**: Matomo data extraction → Transformation → Loading into PostgreSQL

#### **4. Train ML Models**
```bash
cd partie2/notebooks
jupyter notebook ml_conversion_prediction.ipynb
```
**Output**:
- 🤖 **Logistic Regression**: Accuracy = **75%**, AUC-ROC = **0.82**
- 🌲 **Random Forest**: Accuracy = **78%**, AUC-ROC = **0.85** ⭐ Best performer
- 📊 **Top Features**: `time_on_site` (28%), `added_to_cart` (24%), `pages_viewed` (18%)

---

## 📊 Detailed Results & Analytics

### **Part 1: Marketing Automation**
| Metric | Value | Insight |
|--------|-------|---------|
| **Emails sent** | 15 | 100% success rate with Brevo API |
| **Posts analyzed** | 30 | Across 4 social platforms |
| **Avg engagement rate** | 5.89% | Facebook top performer (7.2%) |
| **Visualizations** | 9 charts | Matplotlib + Seaborn |

### **Part 2: Data Pipeline & ML**
| Metric | Value | Insight |
|--------|-------|---------|
| **ML dataset** | 1000 users | 11 features, realistic distribution |
| **Conversion rate** | 58.6% | Generated with weighted sampling |
| **Logistic Regression accuracy** | 75% | AUC-ROC = 0.82 |
| **Random Forest accuracy** | 78% | AUC-ROC = 0.85 ⭐ Best model |
| **Top 3 features** | `time_on_site` (28%), `added_to_cart` (24%), `pages_viewed` (18%) | Actionable insights |
| **ETL performance** | 0.15s | 2923 visits, 370 conversions processed |

### **SQL Queries Implemented**
1. ✅ **Conversion Rate by Channel**: `organic` (60%), `paid` (50%), `email` (66%), `social` (50%)
2. ✅ **ARPU (Average Revenue Per User)**: €162.50 overall, detailed by channel
3. ✅ **Top 5 Conversion Hours**: Peak time identification (12h, 15h, 17h)
4. ✅ **Cohort Analysis**: Monthly retention tracking with 100% baseline

---

## ✅ Testing & Validation

### **Data Quality**
- ✅ Email delivery testing with real data (`inscrits.csv`)
- ✅ ML dataset validation (feature distribution analysis)
- ✅ ETL pipeline data integrity checks

### **Model Evaluation**
- ✅ ROC-AUC curves for both models
- ✅ Confusion matrices and classification reports
- ✅ Cross-validation with 5 folds

### **SQL & Database**
- ✅ Execution of 4 analytics queries with test data
- ✅ Database connection testing
- ✅ Verification of visualizations in Jupyter notebooks

---

## 🔧 Tech Stack

### **Core Technologies**
- **Languages**: Python 3.11+
- **Database**: PostgreSQL 13+
- **API Integration**: Brevo (SendinBlue), Matomo Analytics
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Matplotlib, Seaborn
- **Notebooks**: Jupyter, IPython

### **Python Libraries**
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/-Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557c?logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/-Seaborn-9cf?logo=python&logoColor=white)

- **Data Science**: `pandas`, `numpy`, `scikit-learn`
- **Visualization**: `matplotlib`, `seaborn`
- **API**: `requests`, `sib-api-v3-sdk` (Brevo)
- **Database**: `psycopg2-binary`
- **Notebooks**: `jupyter`, `ipykernel`

---

## 🔐 Security & Best Practices

- ⚠️ **Never commit `.env` files** (already in `.gitignore`)
- 🔑 API keys secured via environment variables
- 📝 `.env.example` templates provided for reference
- 🛡️ SQL injection prevention through parameterized queries
- 🔒 Database credentials stored securely

---

## 📈 Key SQL Analytics Queries

1. **Conversion Rate Analysis**: Session-based conversion tracking by marketing channel
2. **ARPU Calculation**: Average revenue per user with channel segmentation
3. **Peak Hours Detection**: Temporal analysis for optimal engagement windows
4. **Cohort Retention**: Monthly cohort analysis for user retention metrics

---

## 📚 Learning Outcomes

This project demonstrates proficiency in:
- **ETL Development**: Building production-ready data pipelines
- **Database Design**: Creating normalized schemas for analytics
- **Machine Learning**: Model training, evaluation, and feature engineering
- **API Integration**: Working with third-party services (Brevo, Matomo)
- **Data Visualization**: Creating meaningful business insights
- **Python Best Practices**: Clean code, error handling, environment management

---

## 🤝 Contact & Feedback

This is an academic project completed as part of data engineering coursework.

**For questions or professional inquiries:**
- 📧 Email: soukaina.elhadifi@gmail.com
- 💼 LinkedIn: [Connect with me](https://www.linkedin.com/in/soukaina-el-hadifi)
- 🌐 Portfolio: [View more projects](https://github.com/eosoukaina)
  
---

## 🎓 Academic Information

**Author**: Soukaina EL Hadifi  
**Institution**: École Nationale des Sciences Appliquées (ENSA)  
**Program**: Engineering Cycle - ID3 (Data Engineering & Analytics)  
**Supervisor**: Prof. Hind Abidi  
**Academic Year**: 2024-2025  
**Status**: ✅ Completed (December 2025)

---

## 📄 License

This project is part of academic coursework and is shared for educational and portfolio purposes.

---

*Last updated: December 2025 | Built with passion for Data Engineering*
