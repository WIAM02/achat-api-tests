from utils.client import client

def test_wrong_endpoint():
    response = client.get("/Achatt")
    assert response.status_code == 400

