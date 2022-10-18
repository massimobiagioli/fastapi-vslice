import pytest

from fastapi_vslice.features.create_device.create_device_form import CreateDeviceForm


@pytest.mark.asyncio
async def test_create_device_form_from_request(new_device_request):
    create_device_form = CreateDeviceForm(new_device_request(
        name='test-device-1',
        address='10.10.10.11'
    ))
    await create_device_form.load_data()

    assert create_device_form.name == 'test-device-1'
    assert create_device_form.address == '10.10.10.11'
    assert create_device_form.validate() is True
    assert create_device_form.errors == []


@pytest.mark.asyncio
async def test_create_device_form_with_missing_name(new_device_request):
    create_device_form = CreateDeviceForm(new_device_request(
        address='10.10.10.1'
    ))
    await create_device_form.load_data()

    assert create_device_form.validate() is False
    assert create_device_form.errors == ['Name is required']


@pytest.mark.asyncio
async def test_create_device_form_with_missing_address(new_device_request):
    create_device_form = CreateDeviceForm(new_device_request(
        name='test-device-1'
    ))
    await create_device_form.load_data()

    assert create_device_form.validate() is False
    assert create_device_form.errors == ['Address is required']


@pytest.mark.asyncio
async def test_create_device_form_with_missing_data(new_device_request):
    create_device_form = CreateDeviceForm(new_device_request())
    await create_device_form.load_data()

    assert create_device_form.validate() is False
    assert create_device_form.errors == [
        'Name is required',
        'Address is required'
    ]
