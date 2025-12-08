"""
TP03 - Exercice 1.1: Script d'automatisation d'envoi d'emails
Module: Web Marketing & CRM
Auteur: SouKaina El Hadifi et Mohamed-Saber El guelta 
Date: Décembre 2025

Ce script automatise l'envoi d'emails de bienvenue via l'API Brevo.
"""

import requests
import csv
import json
from datetime import datetime
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

# Clé API Brevo - À remplacer par votre propre clé
# Pour obtenir votre clé: https://app.brevo.com/settings/keys/api
# IMPORTANT: Ne jamais commit de vraie clé API dans Git !
# Utilisez des variables d'environnement en production
API_KEY = 'votre_clé_api_brevo'  # Remplacez par votre clé API

# URL de l'API Brevo pour l'envoi d'emails
API_URL = 'https://api.brevo.com/v3/smtp/email'

# Configuration de l'expéditeur
SENDER_EMAIL = 'hello@startup.com'
SENDER_NAME = 'Startup Team'

# ============================================================================
# FONCTIONS
# ============================================================================

def create_email_payload(email, prenom, date_inscription):
    """
    Crée le payload JSON pour l'envoi d'un email personnalisé.
    
    Args:
        email (str): Email du destinataire
        prenom (str): Prénom du destinataire
        date_inscription (str): Date d'inscription
    
    Returns:
        dict: Payload formaté pour l'API Brevo
    """
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .content {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #4CAF50;
                border-bottom: 3px solid #4CAF50;
                padding-bottom: 10px;
            }}
            .highlight {{
                color: #4CAF50;
                font-weight: bold;
            }}
            .footer {{
                margin-top: 20px;
                padding-top: 20px;
                border-top: 1px solid #ddd;
                font-size: 12px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="content">
                <h1> Bienvenue {prenom} !</h1>
                <p>Bonjour <span class="highlight">{prenom}</span>,</p>
                <p>Nous sommes ravis de vous accueillir dans notre communauté !</p>
                <p>Votre inscription a été effectuée le <strong>{date_inscription}</strong>.</p>
                <p>Voici ce que vous pouvez faire maintenant :</p>
                <ul>
                    <li> Découvrir nos services</li>
                    <li> Personnaliser votre profil</li>
                    <li> Rejoindre notre communauté</li>
                    <li> Commencer votre aventure</li>
                </ul>
                <p>Si vous avez des questions, n'hésitez pas à nous contacter !</p>
                <div class="footer">
                    <p>Cordialement,<br>L'équipe Startup</p>
                    <p><em>Cet email a été envoyé automatiquement via l'API Brevo - TP03 Web Marketing & CRM</em></p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    payload = {
        'sender': {
            'email': SENDER_EMAIL,
            'name': SENDER_NAME
        },
        'to': [
            {
                'email': email,
                'name': prenom
            }
        ],
        'subject': f' Bienvenue {prenom} dans notre communauté !',
        'htmlContent': html_content,
        'textContent': f"Bonjour {prenom}, bienvenue dans notre communauté ! Votre inscription a été effectuée le {date_inscription}."
    }
    
    return payload


def send_email(payload):
    """
    Envoie un email via l'API Brevo.
    
    Args:
        payload (dict): Payload de l'email
    
    Returns:
        tuple: (status_code, response_data)
    """
    headers = {
        'accept': 'application/json',
        'api-key': API_KEY,
        'content-type': 'application/json'
    }
    
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=10
        )
        return response.status_code, response.json() if response.text else {}
    except requests.exceptions.RequestException as e:
        return None, {'error': str(e)}


def log_result(email, prenom, status_code, response_data, log_file='email_logs.txt'):
    """
    Enregistre les résultats d'envoi dans un fichier log.
    
    Args:
        email (str): Email du destinataire
        prenom (str): Prénom du destinataire
        status_code (int): Code de statut HTTP
        response_data (dict): Réponse de l'API
        log_file (str): Nom du fichier de log
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(log_file, 'a', encoding='utf-8') as f:
        if status_code == 201:
            f.write(f"[{timestamp}]  SUCCÈS - Email envoyé à {prenom} ({email}) - MessageID: {response_data.get('messageId', 'N/A')}\n")
        else:
            error_msg = response_data.get('message', response_data.get('error', 'Erreur inconnue'))
            f.write(f"[{timestamp}]  ÉCHEC - {prenom} ({email}) - Code: {status_code} - Erreur: {error_msg}\n")


def main():
    """
    Fonction principale qui orchestre l'envoi des emails.
    """
    print("=" * 70)
    print("TP03 - EXERCICE 1.1: AUTOMATISATION D'ENVOI D'EMAILS")
    print("=" * 70)
    print()
    
    # Vérification de la clé API
    if API_KEY == 'votre_clé_api_brevo':
        print("  ATTENTION: Vous devez remplacer 'votre_clé_api_brevo' par votre vraie clé API Brevo!")
        print(" Pour obtenir votre clé: https://app.brevo.com/settings/keys/api")
        print()
        response = input("Voulez-vous continuer quand même (mode test) ? (o/n): ")
        if response.lower() != 'o':
            print(" Arrêt du programme.")
            return
        print("\n⚠️  Mode test activé - Les emails ne seront PAS réellement envoyés.\n")
    
    # Lecture du fichier CSV
    csv_file = 'inscrits.csv'
    
    if not os.path.exists(csv_file):
        print(f" Erreur: Le fichier '{csv_file}' n'existe pas!")
        return
    
    print(f" Lecture du fichier: {csv_file}")
    print()
    
    # Initialisation du fichier de log
    log_file = 'email_logs.txt'
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n{'=' * 70}\n")
        f.write(f"Nouvelle session - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'=' * 70}\n")
    
    # Compteurs de statistiques
    total_emails = 0
    success_count = 0
    error_count = 0
    
    # Traitement des inscrits
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                total_emails += 1
                email = row['email']
                prenom = row['prenom']
                date_inscription = row['date_inscription']
                
                print(f" Envoi à: {prenom} ({email})...")
                
                # Créer le payload
                payload = create_email_payload(email, prenom, date_inscription)
                
                # Envoyer l'email
                status_code, response_data = send_email(payload)
                
                # Logger le résultat
                log_result(email, prenom, status_code, response_data, log_file)
                
                # Afficher le résultat
                if status_code == 201:
                    print(f"    Succès! Code: {status_code}")
                    success_count += 1
                elif status_code is None:
                    print(f"    Erreur de connexion: {response_data.get('error', 'Inconnue')}")
                    error_count += 1
                else:
                    error_msg = response_data.get('message', response_data.get('error', 'Erreur inconnue'))
                    print(f"    Échec! Code: {status_code} - {error_msg}")
                    error_count += 1
                
                print()
                
    except FileNotFoundError:
        print(f" Erreur: Impossible d'ouvrir le fichier '{csv_file}'")
        return
    except KeyError as e:
        print(f" Erreur: Colonne manquante dans le CSV: {e}")
        return
    except Exception as e:
        print(f" Erreur inattendue: {e}")
        return
    
    # Affichage du résumé
    print("=" * 70)
    print(" RÉSUMÉ DE L'ENVOI")
    print("=" * 70)
    print(f"Total d'emails traités: {total_emails}")
    print(f" Succès: {success_count}")
    print(f" Échecs: {error_count}")
    print(f" Taux de réussite: {(success_count/total_emails*100) if total_emails > 0 else 0:.1f}%")
    print(f"\n Les détails sont disponibles dans: {log_file}")
    print("=" * 70)


# ============================================================================
# POINT D'ENTRÉE
# ============================================================================

if __name__ == '__main__':
    main()
