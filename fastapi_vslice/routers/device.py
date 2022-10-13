import uuid

from fastapi import APIRouter, Depends

from fastapi_vslice.shared.database import get_session
from fastapi_vslice.features.create_device.create_device_command import create_device_command_handler, \
    CreateDeviceCommand
from fastapi_vslice.schemas.device import Device, DeviceCreate

router = APIRouter(
    prefix="/devices",
)


@router.post("/", response_model=Device)
async def create_device(
        device: DeviceCreate,
        session=Depends(get_session),
) -> Device:
    return create_device_command_handler(
        command=CreateDeviceCommand(
            device_id=uuid.uuid4(),
            payload=device
        ),
        session=session
    )
