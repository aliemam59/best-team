def test_user_cannot_access_admin(client):
    response = client.get("/admin/dashboard", follow_redirects=True)
    assert b"Login" in response.data
