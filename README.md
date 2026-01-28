# Tests API - Achat

Projet de tests API propre et maintenable.

## 📦 Installation

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Copiez le fichier `.env.example` vers `.env` :
   ```bash
   cp .env.example .env
   ```

2. Modifiez `.env` avec vos valeurs :
   ```
   BASE_URL=https://dev.consult-it.com
   API_PREFIX=/api/v1
   API_TOKEN=votre_token_ici
   ```
   
   **Note :** Si l'API nécessite une authentification, ajoutez votre token dans `API_TOKEN`. Le client ajoutera automatiquement le header `Authorization: Bearer <token>`.

## 🧪 Lancer les tests

```bash
pytest -v
```

Pour générer un rapport HTML :
```bash
pytest --html=report.html
```

## 📁 Structure

```
achat-api-tests/
│
├── tests/
│   ├── test_achat_get.py      # Tests de succès
│   ├── test_achat_errors.py   # Tests d'erreurs
│
├── utils/
│   ├── config.py              # Configuration depuis .env
│   ├── client.py              # Client API réutilisable
│
├── .env                       # Variables d'environnement (à créer)
├── pytest.ini                 # Configuration pytest
└── requirements.txt           # Dépendances Python
```

## 🔐 Authentification

L'authentification est déjà configurée ! Il suffit d'ajouter votre token dans le fichier `.env` :

```
API_TOKEN=votre_token_ici
```

Le client ajoutera automatiquement le header `Authorization: Bearer <token>` à toutes les requêtes.

