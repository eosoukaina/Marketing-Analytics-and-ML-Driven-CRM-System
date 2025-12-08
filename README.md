
# TP03 - Web Marketing & CRM
## Partie 1: APIs Marketing & Automatisation

**Module:** Web Marketing & CRM  
**Semestre:** 5  
**Année universitaire:** 2025/2026  
**Professeur:** Pr. Sara OUALD CHAIB

---

## 📋 Contenu du Repository

Ce repository contient l'implémentation complète de la **Partie 1** du TP03 :

### 📁 Fichiers du Projet

```
TP03/
├── email_automation.py          # Script d'automatisation d'envoi d'emails (Exercice 1.1)
├── social_media_analysis.ipynb  # Notebook d'analyse des données sociales (Exercice 1.2)
├── inscrits.csv                 # Dataset des inscrits pour l'envoi d'emails
├── social_posts.csv             # Dataset des publications sur les réseaux sociaux
└── README.md                    # Cette documentation
```

---


## 📧 Exercice 1.1 : API Email Marketing

### Description
Script Python qui automatise l'envoi d'emails de bienvenue personnalisés via l'API Brevo.

### Fonctionnalités
- ✉️ Connexion à l'API Brevo avec authentification par clé API
- 📂 Lecture des inscrits depuis un fichier CSV
- 🎨 Envoi d'emails HTML personnalisés avec le prénom et la date d'inscription
- 📝 Logging détaillé des succès et échecs dans un fichier texte
- 📊 Statistiques de campagne (taux de réussite, nombre d'envois)

### Prérequis

1. **Obtenir une clé API Brevo:**
   - Créer un compte gratuit sur [Brevo](https://www.brevo.com/)
   - Accéder aux [paramètres API](https://app.brevo.com/settings/keys/api)
   - Générer une nouvelle clé API
   - Remplacer `votre_clé_api_brevo` dans le script

2. **Installer les dépendances:**
   ```powershell
   pip install requests
   ```

### Utilisation

```powershell
# Exécuter le script
python email_automation.py
```

### Structure du CSV (inscrits.csv)

```csv
email,prenom,date_inscription
jean.dupont@email.com,Jean,2025-01-15
marie.martin@email.com,Marie,2025-01-15
```

### Exemple de sortie

```
======================================================================
TP03 - EXERCICE 1.1: AUTOMATISATION D'ENVOI D'EMAILS
======================================================================

📂 Lecture du fichier: inscrits.csv

📧 Envoi à: Jean (jean.dupont@email.com)...
   ✅ Succès! Code: 201

📧 Envoi à: Marie (marie.martin@email.com)...
   ✅ Succès! Code: 201

======================================================================
📊 RÉSUMÉ DE L'ENVOI
======================================================================
 - Total d'emails traités: 15
 - Succès: 15
 - Échecs: 0
 - Taux de réussite: 100.0%

📝 Les détails sont disponibles dans: email_logs.txt
======================================================================
```

### Concepts Clés Couverts
- API REST et endpoints HTTP
- Authentification par clé API
- Gestion des requêtes HTTP (POST)
- Rate limiting et gestion d'erreurs
- Logging et monitoring

---

## 📊 Exercice 1.2 : Social Media Data Collection & Analysis

### Description
Notebook Jupyter complet pour analyser les performances des publications sur les réseaux sociaux (Instagram, Facebook, LinkedIn, Twitter).

### Fonctionnalités

#### 1. **Chargement et Exploration des Données**
   - Import du dataset CSV
   - Analyse exploratoire (info, describe, valeurs manquantes)
   - Conversion des types de données

#### 2. **Calcul des Métriques Clés**
   - **Engagement Rate:** `(Likes + Comments + Shares) / Reach × 100`
   - **Total Engagement:** Somme des interactions
   - **Impression Rate:** Ratio impressions/reach
   - Extraction des informations temporelles (heure, jour)

#### 3. **Analyses Stratégiques**
   - Statistiques par plateforme
   - Statistiques par type de contenu
   - Analyse des meilleurs horaires de publication
   - Identification des combinaisons gagnantes

#### 4. **Visualisations (9 graphiques)**
   - Distribution des posts par plateforme
   - Engagement Rate moyen par plateforme
   - Reach moyen et évolution temporelle
   - Heatmap Plateforme × Heure
   - Corrélations Reach vs Engagement
   - Box plots des métriques
   - Et plus encore...

#### 5. **Recommandations Automatiques**
   - Meilleure plateforme à prioriser
   - Type de contenu le plus performant
   - Top 3 des heures optimales
   - Combinaisons gagnantes par plateforme

### Prérequis

```powershell
# Installer les dépendances
pip install pandas numpy matplotlib seaborn jupyter
```

### Utilisation

```powershell
# Lancer Jupyter Notebook
jupyter notebook social_media_analysis.ipynb
```

Ou directement dans VS Code avec l'extension Jupyter installée.

### Structure du Dataset (social_posts.csv)

```csv
post_id,date,platform,content_type,likes,comments,shares,reach,impressions
1,2025-01-15 09:00:00,Instagram,carousel,450,23,12,8500,12000
2,2025-01-15 14:00:00,Facebook,image,320,15,8,6200,9500
```

**Colonnes:**
- `post_id`: Identifiant unique du post
- `date`: Date et heure de publication
- `platform`: Plateforme sociale (Instagram, Facebook, LinkedIn, Twitter)
- `content_type`: Type de contenu (image, video, carousel, reel, story, article, text)
- `likes`, `comments`, `shares`: Métriques d'engagement
- `reach`: Nombre de personnes uniques atteintes
- `impressions`: Nombre total d'affichages

### Exemples de Résultats

#### Statistiques Globales
```
-  Engagement Rate moyen: 5.89%
-  Reach moyen: 10,320
-  Impressions totales: 436,200
-  Engagement total: 4,892
```

#### Meilleurs Horaires
```
🏆 Top 5 des meilleures heures:
   16h00 - Engagement Rate: 7.12% (Reach moyen: 17,350)
   11h00 - Engagement Rate: 6.89% (Reach moyen: 13,700)
   10h00 - Engagement Rate: 6.75% (Reach moyen: 15,600)
```

### Exports Générés
- `social_posts_analysed.csv` - Dataset enrichi avec métriques calculées
- `platform_statistics.csv` - Statistiques agrégées par plateforme
- `hourly_statistics.csv` - Statistiques horaires
- `analyse_plateformes.png` - Graphiques d'analyse des plateformes
- `analyse_temporelle.png` - Graphiques d'analyse temporelle
- `analyse_engagement.png` - Graphiques des métriques d'engagement

### Concepts Clés Couverts
- ETL (Extract, Transform, Load)
- Métriques marketing (engagement rate, reach, impressions)
- Analyse exploratoire de données (EDA)
- Visualisation de données avec Matplotlib et Seaborn
- Statistiques descriptives et agrégations
- Time series analysis

---

## 📚 Questions Théoriques (Répondues dans le Notebook)

### 1. Pourquoi utiliser first-party cookies plutôt que third-party ?

**Points clés:**
- ✅ Meilleure conformité RGPD/CCPA
- ✅ Taux de blocage < 5% (vs > 40% pour third-party)
- ✅ Données plus fiables et précises
- ✅ Contrôle total sur les données
- ✅ Meilleure performance du site

### 2. Quelle différence entre pixel synchrone et asynchrone ?

| Critère | Synchrone | Asynchrone |
|---------|-----------|------------|
| **Chargement** | Bloque la page | Non bloquant |
| **Performance** | ❌ Ralentit | ✅ Rapide |
| **UX** | ❌ Impact négatif | ✅ Optimal |
| **Fiabilité** | 100% | 95-98% |

**Recommandation:** Utiliser asynchrone pour améliorer les Core Web Vitals et l'expérience utilisateur.

---

## 🚀 Installation Complète

### Étape 1: Cloner ou télécharger le projet
```powershell
# Si vous utilisez Git
git clone <url-du-repository>
cd TP03
```

### Étape 2: Créer un environnement virtuel (optionnel mais recommandé)
```powershell
# Créer l'environnement
python -m venv venv

# Activer l'environnement
.\venv\Scripts\Activate.ps1
```

### Étape 3: Installer toutes les dépendances
```powershell
pip install requests pandas numpy matplotlib seaborn jupyter
```

### Étape 4: Configurer l'API Brevo
1. Créer un compte sur [Brevo](https://www.brevo.com/)
2. Obtenir la clé API
3. Remplacer dans `email_automation.py`:
   ```python
   API_KEY = 'votre_clé_api_brevo'  # ← Remplacer ici
   ```

### Étape 5: Tester le script d'emails
```powershell
python email_automation.py
```

### Étape 6: Lancer le notebook d'analyse
```powershell
jupyter notebook social_media_analysis.ipynb
```

Ou ouvrir directement dans VS Code avec l'extension Jupyter.

---

## 📊 Structure des Données

### Fichier: inscrits.csv
- **15 inscrits** avec emails, prénoms et dates d'inscription
- Format: `email,prenom,date_inscription`

### Fichier: social_posts.csv
- **30 publications** sur 4 plateformes (Instagram, Facebook, LinkedIn, Twitter)
- **9 colonnes** avec métriques complètes
- Période: 15-24 janvier 2025

---


## 📈 Métriques de Performance

### Script Email Automation
- ⚡ Temps d'exécution: ~3-5 secondes pour 15 emails
- ✅ Taux de réussite attendu: 95-100%
- 📝 Logging complet dans `email_logs.txt`

### Notebook d'Analyse
- 📊 30 publications analysées
- 🎨 9 visualisations générées
- 📁 3 fichiers CSV exportés
- 🖼️ 3 images PNG haute résolution

---


## 👨‍💻 Auteur

- **Soukaina El Hadifi** 
- **Mohamed-Saber Elguelta**  


---


