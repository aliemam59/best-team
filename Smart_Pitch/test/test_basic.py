def test_app_running(client):
    response = client.get("/")
    assert response.status_code == 200
