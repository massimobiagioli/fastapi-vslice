import uuid

import pytest as pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from fastapi_vslice.features.create_device.create_device_command import create_device_command_handler, \
    CreateDeviceCommand
from fastapi_vslice.main import app
from fastapi_vslice.schemas.device import DeviceCreate
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
def devices(session):
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
