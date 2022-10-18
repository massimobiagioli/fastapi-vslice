import asyncio
import uuid

import pytest as pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from fastapi_vslice.features.activate_device.activate_device_command import activate_device_command_handler, \
    ActivateDeviceCommand
from fastapi_vslice.features.create_device.create_device_command import create_device_command_handler, \
    CreateDeviceCommand
from fastapi_vslice.main import app
from fastapi_vslice.schemas.device import DeviceCreate, Device
from fastapi_vslice.shared.database import Base, SQLALCHEMY_DATABASE_TEST_URL, get_session


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_TEST_URL)
    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def session(db_engine):
    connection = db_engine.connect()
    connection.begin()
    session = Session(bind=connection)
    yield session
    session.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(session):
    app.dependency_overrides[get_session] = lambda: session
    with TestClient(app) as c:
        yield c


@pytest.fixture
def create_devices(session):
    create_device_command_handler(
        CreateDeviceCommand(
            uuid.UUID("c0a80101-0000-0000-0000-000000000001"),
            DeviceCreate(
                name="device-1",
                address="10.10.10.1"
            )
        ),
        session
    )
    create_device_command_handler(
        CreateDeviceCommand(
            uuid.UUID("c0a80101-0000-0000-0000-000000000002"),
            DeviceCreate(
                name="device-2",
                address="10.10.10.2"
            )
        ),
        session
    )


@pytest.fixture
def create_activated_device(session):
    create_device_command_handler(
        CreateDeviceCommand(
            uuid.UUID("c0a80101-0000-0000-0000-000000000001"),
            DeviceCreate(
                name="device-1",
                address="10.10.10.1"
            )
        ),
        session
    )
    activate_device_command_handler(
        ActivateDeviceCommand(
            uuid.UUID("c0a80101-0000-0000-0000-000000000001")
        ),
        session
    )


@pytest.fixture
def new_device_request(mocker):
    def _new_device_request(name: str = None, address: str = None):
        form_future = asyncio.Future()
        form_future.set_result({
            'name': name,
            'address': address
        })
        request = mocker.MagicMock()
        request.form = mocker.MagicMock(return_value=form_future)
        return request

    return _new_device_request
