import os
from pathlib import Path
from dotenv import load_dotenv

# Trouver le répertoire racine du projet (où se trouve .env)
PROJECT_ROOT = Path(__file__).parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

# Charger le fichier .env depuis le répertoire racine
load_dotenv(dotenv_path=ENV_FILE)

BASE_URL = os.getenv("BASE_URL")
API_PREFIX = os.getenv("API_PREFIX")
API_TOKEN = os.getenv("API_TOKEN", "")  # Optionnel, vide par défaut

if not BASE_URL:
    raise RuntimeError("BASE_URL missing")

