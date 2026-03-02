#!/usr/bin/env python3
"""
Script de ping pour réveiller le serveur Render
Exécuté 2 fois par jour à 9h00 et 9h09
"""

import requests
import time
import os
import sys
from datetime import datetime

# URL de votre serveur Render
RENDER_URL = os.environ.get('RENDER_URL', 'https://collecteur-de-questions-render.onrender.com')
PING_URL = f"{RENDER_URL}/ping"

def ping_server():
    """Effectue un ping simple vers le serveur"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"🔔 [{timestamp}] Ping vers {PING_URL}")
    
    try:
        # Timeout de 30 secondes
        response = requests.get(PING_URL, timeout=30)
        
        if response.status_code == 200:
            print(f"✅ Succès! Code: {response.status_code}")
            print(f"📦 Réponse: {response.text[:100]}")
            return True
        else:
            print(f"⚠️ Échec! Code: {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        print("⏳ Timeout - Le serveur met du temps à répondre")
        return False
    except requests.exceptions.ConnectionError:
        print("🔌 Erreur de connexion - Serveur inaccessible")
        return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def main():
    """Point d'entrée principal"""
    print("=" * 50)
    print("🚀 DÉMARRAGE DU PING RENDER")
    print(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 {RENDER_URL}")
    print("=" * 50)
    
    success = ping_server()
    
    if success:
        print("✅ Ping terminé avec succès")
        sys.exit(0)
    else:
        print("❌ Échec du ping")
        sys.exit(1)

if __name__ == "__main__":
    main()
