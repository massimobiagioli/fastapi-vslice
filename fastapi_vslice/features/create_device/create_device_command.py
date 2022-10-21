import uuid
from dataclasses import dataclass
from operator import or_
from typing import Optional

from sqlalchemy.orm import Session

from fastapi_vslice.models.device import Device as DeviceModel
from fastapi_vslice.schemas.device import Device, DeviceCreate


class CreateDeviceException(Exception):
    pass


@dataclass
class CreateDeviceCommand:
    device_id: uuid.UUID
    payload: DeviceCreate


@dataclass
class CreateDeviceResult:
    device: Optional[Device] = None
    error_message: Optional[str] = None

    def got_error(self) -> bool:
        return self.error_message is not None


def create_device_command_handler(
    command: CreateDeviceCommand, session: Session
) -> CreateDeviceResult:
    q = session.query(DeviceModel).filter(
        or_(
            DeviceModel.name == command.payload.name,
            DeviceModel.address == command.payload.address,
        )
    )

    if session.query(q.exists()).scalar():
        return CreateDeviceResult(error_message="Device already exists")

    new_device = DeviceModel(id=str(command.device_id), **command.payload.dict())

    session.add(new_device)
    session.commit()
    session.refresh(new_device)
    return CreateDeviceResult(device=new_device)
