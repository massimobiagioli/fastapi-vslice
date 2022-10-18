from http import HTTPStatus
import uuid
from typing import List

from fastapi import APIRouter, Depends

from fastapi_vslice.features.create_device.create_device_command import create_device_command_handler, \
    CreateDeviceCommand
from fastapi_vslice.features.list_devices.list_devices_query import list_devices_query
from fastapi_vslice.schemas.device import Device, DeviceCreate
from fastapi_vslice.shared.database import get_session

router = APIRouter(
    prefix="/api/devices",
)


@router.get("/", response_model=List[Device])
async def get_devices(session=Depends(get_session)) -> List[Device]:
    return list_devices_query(session=session)


@router.post("/", response_model=Device, status_code=HTTPStatus.CREATED)
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
