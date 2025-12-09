"""
TP03 - Partie 2 - Exercice 2.1.2
Pipeline ETL pour extraction, transformation et chargement de données marketing
Auteur: - Soukaina El Hadifi 
        - Mohamed-Saber El guelta
Date: Décembre 2025

Ce script:
- Extrait les données depuis Matomo API ( ou source simulée)
- Transforme et nettoie les données
- Charge dans PostgreSQL
- Peut être schedulé avec cron/Task Scheduler
"""

import requests
import psycopg2
from psycopg2 import sql
from datetime import datetime, timedelta
import json
import logging
from typing import Dict, List, Optional
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

# Configuration PostgreSQL
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'marketing_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', '0000')
}

# Configuration Matomo API (simulée pour le TP)
MATOMO_CONFIG = {
    'url': 'https://demo.matomo.cloud',
    'site_id': '1',
    'token_auth': 'anonymous',  # À remplacer par votre token
    'method': 'VisitsSummary.get',
    'period': 'day',
    'date': 'today'
}

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('etl_pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ============================================================================
# FONCTIONS EXTRACT
# ============================================================================

def extract_from_matomo_api() -> Optional[Dict]:
    """
    Extrait les données depuis l'API Matomo
    
    Returns:
        Dict contenant les métriques ou None en cas d'erreur
    """
    logger.info("📥 EXTRACT: Récupération des données depuis Matomo API...")
    
    try:
        params = {
            'module': 'API',
            'method': MATOMO_CONFIG['method'],
            'idSite': MATOMO_CONFIG['site_id'],
            'period': MATOMO_CONFIG['period'],
            'date': MATOMO_CONFIG['date'],
            'format': 'json',
            'token_auth': MATOMO_CONFIG['token_auth']
        }
        
        response = requests.get(
            f"{MATOMO_CONFIG['url']}/index.php",
            params=params,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Données extraites: {len(data)} métriques")
            return data
        else:
            logger.error(f"Erreur API: {response.status_code}")
            return None
            
    except requests.RequestException as e:
        logger.error(f"Erreur de connexion: {e}")
        return None

def extract_simulated_data() -> Dict:
    """
    Génère des données simulées pour le TP (si pas d'accès à l'API)
    
    Returns:
        Dict contenant des métriques simulées
    """
    logger.info("EXTRACT: Génération de données simulées...")
    
    import random
    
    data = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'nb_visits': random.randint(1000, 5000),
        'nb_actions': random.randint(3000, 15000),
        'nb_visits_converted': random.randint(50, 500),
        'bounce_count': random.randint(200, 1000),
        'sum_visit_length': random.randint(50000, 200000),
        'max_actions': random.randint(10, 50),
        'bounce_rate': f"{random.randint(20, 60)}%",
        'nb_actions_per_visit': random.uniform(2, 6),
        'avg_time_on_site': random.randint(60, 300)
    }
    
    logger.info(f"Données simulées générées: {data['nb_visits']} visites")
    return data

# ============================================================================
# FONCTIONS TRANSFORM
# ============================================================================

def transform_data(raw_data: Dict) -> Dict:
    """
    Transforme et nettoie les données brutes
    
    Args:
        raw_data: Données brutes de l'API
        
    Returns:
        Dict avec données nettoyées et enrichies
    """
    logger.info("TRANSFORM: Transformation des données...")
    
    try:
        # Nettoyage et normalisation
        transformed = {
            'date': datetime.now(),
            'visits': int(raw_data.get('nb_visits', 0)),
            'conversions': int(raw_data.get('nb_visits_converted', 0)),
            'actions': int(raw_data.get('nb_actions', 0)),
            'bounce_count': int(raw_data.get('bounce_count', 0)),
            'total_time': int(raw_data.get('sum_visit_length', 0))
        }
        
        # Calculs de métriques dérivées
        if transformed['visits'] > 0:
            transformed['conversion_rate'] = round(
                (transformed['conversions'] / transformed['visits']) * 100, 2
            )
            transformed['bounce_rate'] = round(
                (transformed['bounce_count'] / transformed['visits']) * 100, 2
            )
            transformed['avg_time_per_visit'] = round(
                transformed['total_time'] / transformed['visits'], 2
            )
            transformed['actions_per_visit'] = round(
                transformed['actions'] / transformed['visits'], 2
            )
        else:
            transformed['conversion_rate'] = 0
            transformed['bounce_rate'] = 0
            transformed['avg_time_per_visit'] = 0
            transformed['actions_per_visit'] = 0
        
        # Validation des données
        if transformed['conversions'] > transformed['visits']:
            logger.warning("ATTENTION: Anomalie: conversions > visites, ajustement...")
            transformed['conversions'] = transformed['visits']
        
        logger.info(f"Transformation terminée: {len(transformed)} champs")
        return transformed
        
    except Exception as e:
        logger.error(f"Erreur transformation: {e}")
        raise

# ============================================================================
# FONCTIONS LOAD
# ============================================================================

def get_db_connection():
    """Crée une connexion à PostgreSQL"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        logger.error(f"Erreur connexion PostgreSQL: {e}")
        raise

def create_table_if_not_exists(conn):
    """Crée la table daily_metrics si elle n'existe pas"""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS daily_metrics (
        id SERIAL PRIMARY KEY,
        date TIMESTAMP NOT NULL,
        visits INTEGER DEFAULT 0,
        conversions INTEGER DEFAULT 0,
        conversion_rate DECIMAL(5,2) DEFAULT 0,
        actions INTEGER DEFAULT 0,
        actions_per_visit DECIMAL(5,2) DEFAULT 0,
        bounce_count INTEGER DEFAULT 0,
        bounce_rate DECIMAL(5,2) DEFAULT 0,
        total_time INTEGER DEFAULT 0,
        avg_time_per_visit DECIMAL(10,2) DEFAULT 0,
        created_at TIMESTAMP DEFAULT NOW(),
        UNIQUE(date)
    );
    
    CREATE INDEX IF NOT EXISTS idx_daily_metrics_date ON daily_metrics(date);
    """
    
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        logger.info("Table daily_metrics vérifiée/créée")
    except psycopg2.Error as e:
        logger.error(f"Erreur création table: {e}")
        conn.rollback()
        raise

def load_to_database(conn, data: Dict) -> bool:
    """
    Charge les données transformées dans PostgreSQL
    
    Args:
        conn: Connexion PostgreSQL
        data: Données à insérer
        
    Returns:
        True si succès, False sinon
    """
    logger.info("LOAD: Chargement dans PostgreSQL...")
    
    insert_query = """
    INSERT INTO daily_metrics (
        date, visits, conversions, conversion_rate, actions, 
        actions_per_visit, bounce_count, bounce_rate, 
        total_time, avg_time_per_visit
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
    ON CONFLICT (date) DO UPDATE SET
        visits = EXCLUDED.visits,
        conversions = EXCLUDED.conversions,
        conversion_rate = EXCLUDED.conversion_rate,
        actions = EXCLUDED.actions,
        actions_per_visit = EXCLUDED.actions_per_visit,
        bounce_count = EXCLUDED.bounce_count,
        bounce_rate = EXCLUDED.bounce_rate,
        total_time = EXCLUDED.total_time,
        avg_time_per_visit = EXCLUDED.avg_time_per_visit,
        created_at = NOW();
    """
    
    try:
        cursor = conn.cursor()
        cursor.execute(insert_query, (
            data['date'],
            data['visits'],
            data['conversions'],
            data['conversion_rate'],
            data['actions'],
            data['actions_per_visit'],
            data['bounce_count'],
            data['bounce_rate'],
            data['total_time'],
            data['avg_time_per_visit']
        ))
        conn.commit()
        cursor.close()
        
        logger.info(f"Données chargées: {data['visits']} visites, {data['conversions']} conversions")
        return True
        
    except psycopg2.Error as e:
        logger.error(f"Erreur chargement: {e}")
        conn.rollback()
        return False

# ============================================================================
# PIPELINE PRINCIPAL
# ============================================================================

def run_etl_pipeline(use_simulated=True):
    """
    Exécute le pipeline ETL complet
    
    Args:
        use_simulated: Si True, utilise des données simulées
    """
    logger.info("=" * 70)
    logger.info("DÉMARRAGE DU PIPELINE ETL")
    logger.info("=" * 70)
    
    start_time = datetime.now()
    
    try:
        # 1. EXTRACT
        if use_simulated:
            raw_data = extract_simulated_data()
        else:
            raw_data = extract_from_matomo_api()
        
        if not raw_data:
            logger.error("Échec de l'extraction, arrêt du pipeline")
            return False
        
        # 2. TRANSFORM
        transformed_data = transform_data(raw_data)
        
        # 3. LOAD
        try:
            conn = get_db_connection()
            create_table_if_not_exists(conn)
            success = load_to_database(conn, transformed_data)
            conn.close()
            
            if not success:
                return False
                
        except Exception as e:
            logger.error(f"Erreur database: {e}")
            logger.info("NOTE: Assurez-vous que PostgreSQL est installé et configuré")
            return False
        
        # Statistiques
        duration = (datetime.now() - start_time).total_seconds()
        
        logger.info("=" * 70)
        logger.info("PIPELINE ETL TERMINÉ AVEC SUCCÈS")
        logger.info(f"Durée d'exécution: {duration:.2f}s")
        logger.info(f"Métriques traitées:")
        logger.info(f"   - Visites: {transformed_data['visits']}")
        logger.info(f"   - Conversions: {transformed_data['conversions']} ({transformed_data['conversion_rate']}%)")
        logger.info(f"   - Taux de rebond: {transformed_data['bounce_rate']}%")
        logger.info("=" * 70)
        
        return True
        
    except Exception as e:
        logger.error(f"Erreur pipeline: {e}")
        logger.exception("Détails de l'erreur:")
        return False

# ============================================================================
# POINT D'ENTRÉE
# ============================================================================

if __name__ == '__main__':
    print("\nConfiguration:")
    print(f"   - Mode: Données simulées (pas d'API réelle)")
    print(f"   - Database: {DB_CONFIG['database']}@{DB_CONFIG['host']}")
    print()
    
    # Exécuter le pipeline
    success = run_etl_pipeline(use_simulated=True)
    
    if success:
        print("\nPipeline exécuté avec succès!")
        print("NOTE: Pour automatiser:")
        print("   Linux/Mac: Ajouter à crontab: 0 * * * * python etl_pipeline.py")
        print("   Windows: Créer une tâche dans Task Scheduler")
    else:
        print("\nLe pipeline a échoué. Vérifiez les logs.")
