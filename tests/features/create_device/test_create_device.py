def test_create_device(client):
    response = client.post("/api/devices/", json={
        "name": "new device",
        "address": "10.10.10.10"
    })
    response_model = response.json()

    assert response.status_code == 201
    assert response_model["id"] is not None
    assert len(response_model["id"]) == 36
    assert response_model["name"] == "new device"
    assert response_model["address"] == "10.10.10.10"
    assert response_model["is_active"] is False
