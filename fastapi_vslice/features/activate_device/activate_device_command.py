import uuid
from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session

from fastapi_vslice.models.device import Device as DeviceModel
from fastapi_vslice.schemas.device import Device


@dataclass
class ActivateDeviceCommand:
    device_id: uuid.UUID


def activate_device_command_handler(
        command: ActivateDeviceCommand,
        session: Session
) -> Device:
    device = session.get(DeviceModel, str(command.device_id))
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    device.is_active = True
    session.add(device)
    session.commit()
    session.refresh(device)
    return device
