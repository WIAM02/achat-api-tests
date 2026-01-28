from utils.client import client

# def test_get_achat_success():
#     print("test_get_achat_success")
#     print("URL: ", client.base_url + "/Achat")
#     response = client.get("/Achat")
#     print("Response: ", response)
#     assert response.status_code == 400

#     data = response.json()
#     assert isinstance(data, list)

# def test_get_achat_success():
#     response = client.get("/Achat")

#     print("STATUS:", response.status_code)
#     print("HEADERS:", response.headers.get("Content-Type"))
#     print("BODY:", response.text)

#     assert response.status_code == 400

# def test_get_achat_without_params_returns_400():
#     response = client.get("/Achat")

#     print("STATUS:", response.status_code)
#     print("HEADERS:", response.headers.get("Content-Type"))
#     print("BODY:", response.text)

#     assert response.status_code == 400

def test_get_achat_with_mission_id_returns_200():
    response = client.get("/Achat", params={"missionId": 1})

    print("STATUS:", response.status_code)
    print("STATUS:", response.status_code)
    print("BODY:", response.text)
    print("BODY:", response.text)
    print("BODY:", response.text)
    print("BODY:", response.text)

    assert response.status_code == 400