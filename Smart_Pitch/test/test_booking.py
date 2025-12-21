def test_booking_page_access(client):
    response = client.get("/booking/search")
    assert response.status_code in [200, 302]
