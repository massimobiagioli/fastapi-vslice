def test_list_all_devices(devices, client):
    response = client.get("/api/devices")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json() == [
        {
            "id": "c0a80101-0000-0000-0000-000000000001",
            "name": "device-1",
            "address": "10.10.10.1",
            "is_active": False
        },
        {
            "id": "c0a80101-0000-0000-0000-000000000002",
            "name": "device-2",
            "address": "10.10.10.2",
            "is_active": False
        }
    ]
