"""
TP03 - Partie 2 - Exercice 2.2.1
Script de génération de données pour le modèle ML de prédiction de conversion
Auteur: [Votre Nom]
Date: Décembre 2025
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration
np.random.seed(42)
random.seed(42)

# Nombre d'utilisateurs à générer
N_USERS = 1000

print("=" * 70)
print("GÉNÉRATION DU DATASET ML - USER BEHAVIOR")
print("=" * 70)
print(f"\nGénération de {N_USERS} utilisateurs...")

# Listes pour la génération aléatoire
sources = ['organic', 'paid', 'email', 'social', 'direct', 'referral']
devices = ['desktop', 'mobile', 'tablet']
browsers = ['chrome', 'firefox', 'safari', 'edge']

# Pondérations réalistes pour les sources
source_weights = [0.35, 0.25, 0.15, 0.15, 0.07, 0.03]

# Pondérations pour les appareils
device_weights = [0.45, 0.45, 0.10]

def generate_user_behavior():
    """Génère les données de comportement d'un utilisateur"""
    
    # Source de trafic (influence la conversion)
    source = random.choices(sources, weights=source_weights)[0]
    
    # Appareil (influence la conversion)
    device = random.choices(devices, weights=device_weights)[0]
    
    # Navigateur
    browser = random.choice(browsers)
    
    # Temps sur le site (secondes) - varie selon la source
    if source == 'paid':
        time_on_site = np.random.gamma(shape=2, scale=60)  # Plus court pour paid
    elif source == 'organic':
        time_on_site = np.random.gamma(shape=3, scale=80)  # Plus long pour organic
    elif source == 'email':
        time_on_site = np.random.gamma(shape=2.5, scale=70)
    else:
        time_on_site = np.random.gamma(shape=2, scale=50)
    
    time_on_site = max(10, min(600, time_on_site))  # Entre 10s et 10min
    
    # Pages vues - corrélé avec le temps sur le site
    base_pages = time_on_site / 60  # ~1 page par minute
    pages_viewed = int(np.random.poisson(base_pages) + 1)
    pages_viewed = max(1, min(20, pages_viewed))
    
    # Jour de la semaine (0 = Lundi, 6 = Dimanche)
    day_of_week = random.randint(0, 6)
    
    # Heure de la journée (influence la conversion)
    hour_of_day = random.choices(
        range(24),
        weights=[2, 1, 1, 1, 1, 2, 4, 6, 8, 10, 12, 12, 10, 9, 10, 12, 14, 15, 13, 10, 8, 6, 4, 3]
    )[0]
    
    # Nombre de visites précédentes
    previous_visits = np.random.poisson(2)
    previous_visits = min(previous_visits, 10)
    
    # Ajout au panier (indicateur fort de conversion)
    added_to_cart = random.random() < 0.3  # 30% ajoutent au panier
    
    # Calcul de la probabilité de conversion basée sur les features
    conversion_prob = 0.05  # Base
    
    # Source (l'email et organic convertissent mieux)
    if source == 'email':
        conversion_prob += 0.15
    elif source == 'organic':
        conversion_prob += 0.12
    elif source == 'paid':
        conversion_prob += 0.08
    elif source == 'social':
        conversion_prob += 0.06
    
    # Appareil (desktop converti mieux)
    if device == 'desktop':
        conversion_prob += 0.10
    elif device == 'mobile':
        conversion_prob += 0.05
    
    # Temps sur le site (plus de temps = plus de conversion)
    if time_on_site > 180:
        conversion_prob += 0.15
    elif time_on_site > 120:
        conversion_prob += 0.10
    elif time_on_site > 60:
        conversion_prob += 0.05
    
    # Pages vues
    if pages_viewed >= 5:
        conversion_prob += 0.12
    elif pages_viewed >= 3:
        conversion_prob += 0.08
    
    # Heure (les heures de bureau convertissent mieux)
    if 9 <= hour_of_day <= 17:
        conversion_prob += 0.08
    
    # Visites précédentes (fidélité)
    if previous_visits >= 3:
        conversion_prob += 0.10
    elif previous_visits >= 1:
        conversion_prob += 0.05
    
    # Ajout au panier (fort indicateur)
    if added_to_cart:
        conversion_prob += 0.25
    
    # Jour de la semaine (semaine > weekend)
    if day_of_week < 5:  # Lundi à Vendredi
        conversion_prob += 0.05
    
    # Limiter la probabilité entre 0 et 1
    conversion_prob = min(0.95, max(0.01, conversion_prob))
    
    # Déterminer la conversion
    converted = 1 if random.random() < conversion_prob else 0
    
    return {
        'user_id': f'user_{random.randint(10000, 99999)}',
        'time_on_site': round(time_on_site, 2),
        'pages_viewed': pages_viewed,
        'source': source,
        'device': device,
        'browser': browser,
        'day_of_week': day_of_week,
        'hour_of_day': hour_of_day,
        'previous_visits': previous_visits,
        'added_to_cart': int(added_to_cart),
        'converted': converted
    }

# Génération des données
data = [generate_user_behavior() for _ in range(N_USERS)]

# Création du DataFrame
df = pd.DataFrame(data)

# Statistiques
print(f"\nDonnées générées avec succès!")
print(f"\nStatistiques du dataset:")
print(f"  - Total utilisateurs: {len(df)}")
print(f"  - Conversions: {df['converted'].sum()} ({df['converted'].mean()*100:.1f}%)")
print(f"  - Non-conversions: {(1-df['converted']).sum()} ({(1-df['converted'].mean())*100:.1f}%)")

print(f"\nDistribution par source:")
print(df['source'].value_counts())

print(f"\nDistribution par appareil:")
print(df['device'].value_counts())

print(f"\nTaux de conversion par source:")
conversion_by_source = df.groupby('source')['converted'].mean() * 100
for source, rate in conversion_by_source.items():
    print(f"  - {source}: {rate:.1f}%")

print(f"\nTaux de conversion par appareil:")
conversion_by_device = df.groupby('device')['converted'].mean() * 100
for device, rate in conversion_by_device.items():
    print(f"  - {device}: {rate:.1f}%")

# Sauvegarde
output_path = '../data/user_behavior.csv'
df.to_csv(output_path, index=False)
print(f"\nDataset sauvegardé: {output_path}")

# Aperçu des données
print(f"\nAperçu des données:")
print(df.head(10))

print(f"\n" + "=" * 70)
print("GÉNÉRATION TERMINÉE")
print("=" * 70)
