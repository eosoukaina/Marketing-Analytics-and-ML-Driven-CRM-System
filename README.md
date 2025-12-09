# 🚀 TP03 - Web Marketing & CRM + ML Analytics

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Analytics-336791?logo=postgresql)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Completed-success)

Projet complet de Web Marketing, CRM, et Machine Learning pour l'analyse et la prédiction des conversions clients.

---

## 🎯 Réalisations du Projet

### **✅ Partie 1 - Web Marketing & CRM**
| Livrables | Statut | Fichiers |
|-----------|--------|----------|
| Script d'automatisation emails (Brevo API) | ✅ Complété | `partie1/src/email_automation.py` |
| Notebook analyse réseaux sociaux | ✅ Complété | `partie1/notebooks/social_media_analysis.ipynb` |
| Visualisations (9 graphiques) | ✅ Complété | `partie1/outputs/social_analysis/` |
| Dataset CSV (15 inscrits + 30 posts) | ✅ Complété | `partie1/data/*.csv` |

### **✅ Partie 2 - ML Pipeline & Analytics**
| Livrables | Statut | Fichiers |
|-----------|--------|----------|
| Schéma PostgreSQL + 4 requêtes SQL | ✅ Complété | `partie2/sql/analytics_queries.sql` |
| Pipeline ETL (Extract-Transform-Load) | ✅ Complété | `partie2/scripts/etl_pipeline.py` |
| Génération dataset ML (1000 users) | ✅ Complété | `partie2/scripts/generate_ml_data.py` |
| Notebook ML (2 modèles) | ✅ Complété | `partie2/notebooks/ml_conversion_prediction.ipynb` |
| Tests de connexion PostgreSQL | ✅ Complété | Tests validés |

### **📊 Résultats Quantitatifs**
- **Partie 1** : 15 emails envoyés, 30 posts analysés, taux engagement 5.89%
- **Partie 2** : 1000 users générés, 78% accuracy ML, 4 requêtes SQL fonctionnelles
- **Temps d'exécution ETL** : 0.15s (optimisé)

---

## 📚 Structure du Projet

```
TP03/
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
│
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

## 🎯 Objectifs du Projet

### **Partie 1 : Web Marketing & CRM**
- ✅ Automatiser l'envoi d'emails personnalisés via **Brevo API**
- ✅ Analyser les performances des réseaux sociaux (engagement, reach)
- ✅ Générer des visualisations et rapports statistiques

### **Partie 2 : ML Pipeline & Analytics**
- ✅ Créer un schéma PostgreSQL pour l'analytics
- ✅ Développer des requêtes SQL avancées (conversion rate, ARPU, cohort)
- ✅ Construire un pipeline ETL (Matomo → Database)
- ✅ Entraîner des modèles ML pour prédire les conversions (Logistic Regression + Random Forest)

---

## 🛠️ Installation

### **Prérequis**
- Python 3.11+
- PostgreSQL 13+ ([Télécharger ici](https://www.postgresql.org/download/))
- Compte Brevo ([Inscription gratuite](https://www.brevo.com/))
- Git

### **1. Cloner le repository**
```bash
git clone https://github.com/eosoukaina/TP03-Web-Marketing-CRM-Partie1.git
cd TP03
```

### **2. Créer l'environnement virtuel**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
```

### **3. Installer les dépendances**
```bash
pip install -r requirements.txt
```

### **4. Configurer les variables d'environnement**

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
MATOMO_API_URL=https://votre-instance.matomo.cloud/
MATOMO_TOKEN=votre_token_matomo
```

> **Note :** Des fichiers `.env.example` sont fournis comme templates dans chaque dossier.

---

## 🚀 Utilisation

### **Partie 1 : Web Marketing & CRM**

#### **1. Automatisation des Emails**
```bash
cd partie1/src
python email_automation.py
```
**Résultats** : Envoi de 15 emails personnalisés + log JSON dans `data/email_results.json`

#### **2. Analyse des Réseaux Sociaux**
```bash
cd partie1/notebooks
jupyter notebook social_media_analysis.ipynb
```
**Résultats** :
- 📊 9 visualisations (engagement par plateforme, distribution des likes, heatmap temporelle)
- 📈 Statistiques : Taux d'engagement moyen = **5.89%**
- 🎯 Meilleure plateforme : **Facebook** (7.2% engagement)

---

### **Partie 2 : ML Pipeline & Analytics**

#### **1. Créer la Base de Données**
```bash
# D'abord, créer la base de données
psql -U postgres -c "CREATE DATABASE marketing_db;"

# Puis charger le schéma et les données
psql -U postgres -d marketing_db -f partie2/sql/analytics_queries.sql
```
**Résultats** : Création des tables `events` et `sessions` + insertion de données de test

#### **2. Générer le Dataset ML**
```bash
cd partie2/scripts
python generate_ml_data.py
```
**Résultats** : Fichier `user_behavior.csv` avec **1000 users** et **11 features**

#### **3. Exécuter le Pipeline ETL**
```bash
python etl_pipeline.py
```
**Résultats** : Extraction des données Matomo → Transformation → Chargement dans PostgreSQL

#### **4. Entraîner les Modèles ML**
```bash
cd partie2/notebooks
jupyter notebook ml_conversion_prediction.ipynb
```
**Résultats** :
- 🤖 **Logistic Regression** : Accuracy = **75%**, AUC-ROC = **0.82**
- 🌲 **Random Forest** : Accuracy = **78%**, AUC-ROC = **0.85**
- 📊 Feature Importance : `time_on_site` (28%), `added_to_cart` (24%), `pages_viewed` (18%)

---

## 📊 Résultats Détaillés

### **Partie 1 : Web Marketing & CRM**
| Métrique | Valeur | Insight |
|----------|--------|---------|
| **Emails envoyés** | 15 | 100% de succès avec Brevo API |
| **Posts analysés** | 30 | Répartis sur 4 plateformes |
| **Taux d'engagement moyen** | 5.89% | Facebook meilleur (7.2%) |
| **Visualisations créées** | 9 graphiques | Matplotlib + Seaborn |

### **Partie 2 : ML Pipeline & Analytics**
| Métrique | Valeur | Insight |
|----------|--------|---------|
| **Dataset ML** | 1000 users | 11 features, distribution réaliste |
| **Taux de conversion** | 58.6% | Généré avec weighted sampling |
| **Accuracy Logistic Regression** | 75% | AUC-ROC = 0.82 |
| **Accuracy Random Forest** | 78% | AUC-ROC = 0.85 (meilleur) |
| **Feature Importance (Top 3)** | `time_on_site` (28%), `added_to_cart` (24%), `pages_viewed` (18%) | Insights actionnables |
| **Performance ETL** | 0.15s | 2923 visites, 370 conversions |

### **Requêtes SQL Implémentées**
1. ✅ **Taux de Conversion par Canal** : `organic` (60%), `paid` (50%), `email` (66%), `social` (50%)
2. ✅ **ARPU (Average Revenue Per User)** : 162.50€ global, détail par canal
3. ✅ **Top 5 Heures de Conversion** : Identification des créneaux optimaux (12h, 15h, 17h)
4. ✅ **Cohort Analysis** : Rétention mensuelle avec 100% mois 0

---

## 💡 Défis Techniques Résolus

### **Partie 1**
1. **Sécurisation des API Keys** : Implémentation de `.env` pour éviter l'exposition des clés Brevo
2. **Gestion des erreurs HTTP** : Logging structuré des échecs d'envoi avec retry logic
3. **Analyse temporelle** : Création de heatmaps pour identifier les heures optimales de publication

### **Partie 2**
1. **Connexion PostgreSQL** : Configuration multi-environnement (dev/prod) avec variables d'environnement
2. **ETL Pipeline** : Gestion des anomalies de données (conversions > visites) avec validation automatique
3. **ML Data Generation** : Distribution réaliste des features avec weighted sampling
4. **Model Optimization** : Comparaison Logistic Regression vs Random Forest avec cross-validation

---

## 🧪 Tests et Validation

### **Partie 1**
- ✅ Test d'envoi d'emails avec données réelles (`inscrits.csv`)
- ✅ Validation des visualisations dans le notebook Jupyter
- ✅ Vérification des logs JSON

### **Partie 2**
- ✅ Exécution des 4 requêtes SQL avec données de test
- ✅ Validation du dataset ML (distribution des features)
- ✅ Évaluation des modèles ML (courbes ROC, matrice de confusion)

---


## 🔧 Technologies Utilisées

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?logo=postgresql&logoColor=white)
![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/-Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557c?logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/-Seaborn-3776AB?logo=python&logoColor=white)

### **Bibliothèques Python**
- **API & Web** : `requests`, `brevo-python`
- **Data Science** : `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Machine Learning** : `scikit-learn`
- **Database** : `psycopg2-binary`
- **Notebooks** : `jupyter`, `ipykernel`

---

## 📝 Requêtes SQL Disponibles

1. **Taux de Conversion** : Calcul du taux de conversion par session
2. **ARPU (Average Revenue Per User)** : Revenu moyen par utilisateur
3. **Top Hours** : Heures de pic d'activité
4. **Cohort Analysis** : Analyse de rétention par cohorte mensuelle

---

## 🔐 Sécurité

- ⚠️ **Ne jamais commiter le fichier `.env`** (déjà dans `.gitignore`)
- 🔑 API Keys sécurisées via variables d'environnement
- 🚫 Fichier `.env.example` fourni comme template

---

## 📸 Aperçus Visuels

### Notebook ML - Courbes ROC
![ROC Curves](partie2/outputs/roc_comparison.png)

### Analyse Réseaux Sociaux - Engagement
![Engagement](partie1/outputs/social_analysis/engagement_by_platform.png)


---

## 🤝 Contribution

Ce projet est un TP académique. Pour toute question ou suggestion :
- 📧 **Soukaina EL Hadifi** : soukaina.elhadifi@gmail.com
- 📧 **Mohamed-Saber Elguelta** : elgueltasaber@gmail.com

---

## 🎓 Auteurs

**Soukaina EL Hadifi** & **Mohamed-Saber Elguelta**  
École Nationale des Sciences Appliquées  
Cycle d'Ingénieur - ID3

---

*Dernière mise à jour : Décembre 2025*

