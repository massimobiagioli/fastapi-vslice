def test_create_device(client):
    response = client.post(
        "/api/devices/", json={"name": "new device", "address": "10.10.10.10"}
    )
    response_model = response.json()

    assert response.status_code == 201
    assert response_model["id"] is not None
    assert len(response_model["id"]) == 36
    assert response_model["name"] == "new device"
    assert response_model["address"] == "10.10.10.10"
    assert response_model["is_active"] is False


def test_error_create_device_with_existing_name(client, create_devices):
    response = client.post(
        "/api/devices/", json={"name": "device-1", "address": "10.10.10.30"}
    )
    response_model = response.json()

    assert response.status_code == 409
    assert response_model["detail"] == "Device already exists"


def test_error_create_device_with_existing_address(client, create_devices):
    response = client.post(
        "/api/devices/", json={"name": "device-999", "address": "10.10.10.1"}
    )
    response_model = response.json()

    assert response.status_code == 409
    assert response_model["detail"] == "Device already exists"
