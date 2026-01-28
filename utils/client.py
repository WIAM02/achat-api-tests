import requests
from utils.config import BASE_URL, API_PREFIX, API_TOKEN

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL.rstrip("/") + API_PREFIX
        self.headers = {
            "Accept": "application/json",
        }
        # Ajouter le token d'authentification si présent
        if API_TOKEN:
            self.headers["Authorization"] = f"Bearer {API_TOKEN}"

    def get(self, path, **kwargs):
        # Fusionner les headers personnalisés avec les headers par défaut
        headers = {**self.headers, **kwargs.pop("headers", {})}
        return requests.get(self.base_url + path, headers=headers, **kwargs)

    def post(self, path, **kwargs):
        # Fusionner les headers personnalisés avec les headers par défaut
        headers = {**self.headers, **kwargs.pop("headers", {})}
        return requests.post(self.base_url + path, headers=headers, **kwargs)

client = APIClient()

