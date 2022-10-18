def test_activate_device(create_activated_device, client):
    response = client.patch("/api/devices/c0a80101-0000-0000-0000-000000000001/deactivate")

    assert response.status_code == 200
    assert response.json()["is_active"] is False


def test_activate_non_existing_device(create_activated_device, client):
    response = client.patch("/api/devices/c0a80101-0000-0000-0000-000000000999/deactivate")

    assert response.status_code == 404
    