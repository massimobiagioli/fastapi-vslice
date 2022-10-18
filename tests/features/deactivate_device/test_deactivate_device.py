def test_activate_devices(create_activated_device, client):
    response = client.patch("/api/devices/c0a80101-0000-0000-0000-000000000001/deactivate")

    assert response.status_code == 200
    assert response.json()["is_active"] is False
