def test_activate_device(create_devices, client):
    response = client.patch("/api/devices/c0a80101-0000-0000-0000-000000000001/activate")

    assert response.status_code == 200
    assert response.json()["is_active"] is True


def test_activate_non_existing_device(create_devices, client):
    response = client.patch("/api/devices/c0a80101-0000-0000-0000-000000000999/activate")

    assert response.status_code == 404

