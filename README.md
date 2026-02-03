# � Marketing Analytics & ML-Driven CRM System

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
| Livrables | Statut | Fichiers |
|-----------|--------|----------|
| Script d'automatisation emails (Brevo API) | ✅ Complété | `partie1/src/email_automation.py` |
| Notebook analyse réseaux sociaux | ✅ Complété | `partie1/notebooks/social_media_analysis.ipynb` |
| Visualisations (9 graphiques) | ✅ Complété | `partie1/outputs/social_analysis/` |
| Dataset CSV (15 inscrits + 30 posts) | ✅ Complété | `partie1/data/*.csv` |

### **✅ Part 2 - Data Engineering & Machine Learning Pipeline**
| Livrables | Statut | Fichiers |
|-----------|--------|----------|
| Schéma PostgreSQL + 4 requêtes SQL | ✅ Complété | `partie2/sql/analytics_queries.sql` |
| Pipeline ETL (Extract-Transform-Load) | ✅ Complété | `partie2/scripts/etl_pipeline.py` |
| Génération dataset ML (1000 users) | ✅ Complété | `partie2/scripts/generate_ml_data.py` |
| Notebook ML (2 modèles) | ✅ Complété | `partie2/notebooks/ml_conversion_prediction.ipynb` |
| Tests de connexion PostgreSQL | ✅ Complété | Tests validés |

### **📊 Key Performance Metrics**
- **Marketing Analytics**: 15 emails sent, 30 social posts analyzed, 5.89% avg engagement rate
- **ML Models**: 1000-user dataset, **78% accuracy** (Random Forest), AUC-ROC 0.85
- **Data Pipeline**: ETL execution time **0.15s** (optimized), 2923 visits processed
- **SQL Analytics**: 4 production-ready queries (conversion rates, ARPU, cohort analysis)

---
�️ Project Structure

```
marketing-analytics-ml-crm/
├── partie1/                          # Marketing Automation & Analytics
├── partie1/                          # Web Marketing & CRM
│   ├── src/
│   │   └── email_automation.py       # Automatisation emails avec Brevo API
│   ├── notebooks/
│   │   └── social_media_analysis.ipynb  # Analyse réseaux sociaux
│   ├── data/
│   │   ├── inscrits.csv              # Base emails (15 inscrits)
│   │   ├── social_posts.csv          # Posts réseaux sociaux (30 posts)
│   │   └── email_results.json        # Résultats envois emails
│   └── outputs/
│       └── social_analysis/          # Graphiques et rapports
│Data Engineering & ML Pipeline
├── partie2/                          # ML Pipeline & Analytics
│   ├── sql/
│   │   └── analytics_queries.sql     # Schéma + 4 requêtes analytics
│   ├── scripts/
│   │   ├── generate_ml_data.py       # Génération dataset ML (1000 users)
│   │   └── etl_pipeline.py           # Pipeline ETL (Matomo → PostgreSQL)
│   ├── notebooks/
│   │   └── ml_conversion_prediction.ipynb  # ML: Logistic + Random Forest
│   └── data/
│       └── user_behavior.csv         # Dataset ML (11 features)
│
├── .env.example                      # Template config API
├── .gitignore                        # Exclusions Git
├── requirements.txt                  # Dépendances Python
└── README.md                         # Documentation (ce fichier)
```

---
Technical Objectives & Skills Demonstrated

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
- ✅ Entraîner des modèles ML pour prédire les conversions (Logistic Regression + Random Forest)

---

## 🛠️ Installation
 the repository**
```bash
git clone https://github.com/eosoukaina/TP03-Web-Marketing-CRM-Partie1.git
cd marketing-analytics-ml-crmreSQL 13+ ([Télécharger ici](https://www.postgresql.org/download/))
- Compte Brevo ([Inscription gratuite](https://www.brevo.com/))
- Git
eate virtual environment**
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

**For Part 1 (Marketing Automation):** Create `.env` at root
```bash
pip install -r requirements.txt
```

### **4. Configurer les variables d'environnement**
For Part 2 (Data Pipeline):** Create `partie2/.env`
**Pour la Partie 1 :** Créer `.env` à la racine :
```env
BREVO_API_KEY=votre_cle_api_brevo
SENDER_EMAIL=hello@startup.com
SENDER_NAME=Startup Team
```

**Pour la Partie 2 :** Créer `partie2/.env` :
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=marketing_db
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
MATOMO_sage Guide

### **Part 1: Marketing Automation & Analytics**

#### **1. Email Automationmple` sont fournis comme templates dans chaque dossier.

---

## 🚀 Utilisation
Output**: 15 personalized emails sent + JSON logs in `data/email_results.json`

#### **2. Social Media Analytics
#### **1. Automatisation des Emails**
```bash
cd partie1/src
python email_automation.py
``Output**:
- 📊 9 visualizations (platform engagement, likes distribution, temporal heatmaps)
- 📈 Statistics: Average engagement rate = **5.89%**
- 🎯 Best performing platform: **Facebook** (7.2% engagement)

---

### **Part 2: Data Engineering & ML Pipeline**

#### **1. Database Setuppar plateforme, distribution des likes, heatmap temporelle)
- 📈 Statistiques : Taux d'engagement moyen = **5.89%**
- 🎯 Meilleure plateforme : **Facebook** (7.2% engagement)

---

### **Partie 2 : ML Pipeline & Analytics**

##Output**: Tables `events` and `sessions` created + test data inserted

#### **2. Generate ML Datasetnées
psql -U postgres -c "CREATE DATABASE marketing_db;"

# Puis charger le schéma et les données
psql -U postgres -d marketing_db -f partie2/sql/analytics_queries.sql
``Output**: `user_behavior.csv` file with **1000 users** and **11 features**

#### **3. Run ETL Pipeline
#### **2. Générer le Dataset ML**
```bash
cd partie2/scripts
python generate_ml_data.py
```
**Résultats** : Fichier `user_behavior.csv` avec **1000 users** et **11 features**

#### **3. Exécuter le Pipeline ETL**
```bash
pyOutput**: Matomo data extraction → Transformation → Loading into PostgreSQL

#### **4. Train ML Modelsnées Matomo → Transformation → Chargement dans PostgreSQL

#### **4. Entraîner les Modèles ML**
```bash
cd partie2/notebooks
juOutput**:
- 🤖 **Logistic Regression**: Accuracy = **75%**, AUC-ROC = **0.82**
- 🌲 **Random Forest**: Accuracy = **78%**, AUC-ROC = **0.85** ⭐ Best performer
- 📊 **Top Features**on** : Accuracy = **75%**, AUC-ROC = **0.82**
- 🌲 **Random Forest** : Accuracy = **78%**, AUC-ROC = **0.85**
- 📊 Feature Importance : `time_on_site` (28%), `added_to_cart` (24%), `pages_viewed` (18%)

---Detailed Results & Analytics

### **Part 1: Marketing Automation
etric | Value | Insight |
|--------|-------|---------|
| **Emails sent** | 15 | 100% success rate with Brevo API |
| **Posts analyzed** | 30 | Across 4 social platforms |
| **Avg engagement rate** | 5.89% | Facebook top performer (7.2%) |
| **Visualizations** | 9 charts | Matplotlib + Seaborn |

### **Part 2: Data Pipeline & MLes | Matplotlib + Seaborn |
etric | Value | Insight |
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
4. ✅ **Cohort Analysis**: Monthly retention tracking with 100% baselineil par canal
3. ✅ **Top 5 Heures de Conversion** : Identification des créneaux optimaux (12h, 15h, 17h)
4. ✅ **Cohort Analysis** : Rétention mensuelle avec 100% mois 0

---Technical Challenges Solved

### **Data Engineering**
1. **PostgreSQL Connection**: Multi-environment configuration (dev/prod) with environment variables
2. **ETL Pipeline Optimization**: Data anomaly handling (conversions > visits) with automated validation
3. **ML Data Generation**: Realistic feature distribution using weighted sampling techniques
4. **Pipeline Performance**: Achieved 0.15s execution time through query optimization

### **Machine Learning**
1. **Model Selection**: Systematic comparison of Logistic Regression vs Random Forest with cross-validation
2. **Feature Engineering**: Identified top predictive features through importance analysis
3. **Class Imbalance**: Handled conversion rate distribution (58.6%) effectively

### **API Integration**
1. **API Key Security**: Implemented `.env` configuration to prevent credential exposure
2. **Erroring & Validation

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
## 🔧 Tech Stackarking
- ✅ Validation des visualisations dans le notebook Jupyter
- ✅ Vérification des logs JSON

### **Partie 2**
- ✅ Exécution des 4 requêtes SQL avec données de test
- ✅ Validation du dataset ML (distribution des features)
- ✅ Évaluation des modèles ML (courbes ROC, matrice de confusion)

---


## 🔧 Technologies Utilisées
Core Technologies**
- **Languages**: Python 3.11+
- **Database**: PostgreSQL 13+
- **API Integration**: Brevo (SendinBlue), Matomo Analytics
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Matplotlib, Seaborn
- **Notebooks**: Jupyter, IPythonadge/-Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557c?logo=python&logoColor=white)
![SeabSQL Analytics Queries

1. **Conversion Rate Analysis**: Session-based conversion tracking by marketing channel
2. **ARPU Calculation**: Average revenue per user with channel segmentation
3. **Peak Hours Detection**: Temporal analysis for optimal engagement windows
4. **Cohort Retention**: Monthly cohort analysis for user retention metrics
- **Database** : `psycopg2-binary`
- **Notebooks** : `jupyter`, `ipykernel`

---ecurity & Best Practices

- ⚠️ **Never commit `.env` files** (already in `.gitignore`)
- 🔑 API keys secured via environment variables
- 📝 `.env.example` templates provided for reference
- 🛡️ SQL injection prevention through parameterized queries
- 🔒 Database credentials stored securelyversion par session
2. **ARPU (Average Revenue Per User)** : Revenu moyen par utilisateur
3. **TVisual Outputs

### ML Model Performance - ROC Curves
---

## Social Media Analytics - Engagement Metrics

- ⚠️ **Ne jamais commiter le fichier `.env`** (déjà dans `.gitignore`)
- 🔑 API Keys sécurisées via variables d'environnement
- 🚫 Fichier `.env.example` fourni comme template
📚 Learning Outcomes

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

*Last updated: December 2025 | Built with ❤️ for Data Engineeringtoute question ou suggestion :
- 📧 **Soukaina EL Hadifi** : soukaina.elhadifi@gmail.com
  
---

## 🎓 Auteurs

**Soukaina EL Hadifi** 
École Nationale des Sciences Appliquées  
Cycle d'Ingénieur - ID3

---

*Dernière mise à jour : Décembre 2025*

