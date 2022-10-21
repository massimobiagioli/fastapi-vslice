import uuid
from dataclasses import dataclass

from sqlalchemy.orm import Session

from fastapi_vslice.models.device import Device as DeviceModel
from fastapi_vslice.schemas.device import Device, DeviceCreate


@dataclass
class CreateDeviceCommand:
    device_id: uuid.UUID
    payload: DeviceCreate


def create_device_command_handler(
    command: CreateDeviceCommand, session: Session
) -> Device:
    new_device = DeviceModel(id=str(command.device_id), **command.payload.dict())

    session.add(new_device)
    session.commit()
    session.refresh(new_device)
    return new_device
