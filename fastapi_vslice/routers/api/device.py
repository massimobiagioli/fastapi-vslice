import uuid
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from fastapi_vslice.features.activate_device.activate_device_command import (
    ActivateDeviceCommand,
    activate_device_command_handler,
)
from fastapi_vslice.features.create_device.create_device_command import (
    CreateDeviceCommand,
    create_device_command_handler,
)
from fastapi_vslice.features.deactivate_device.deactivate_device_command import (
    DeactivateDeviceCommand,
    deactivate_device_command_handler,
)
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
    create_device_result = create_device_command_handler(
        command=CreateDeviceCommand(device_id=uuid.uuid4(), payload=device),
        session=session,
    )

    if create_device_result.got_error():
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail=create_device_result.error_message
        )

    return create_device_result.device


@router.patch("/{device_id}/activate", response_model=Device)
async def activate_device(
    device_id: uuid.UUID,
    session=Depends(get_session),
) -> Device:
    return activate_device_command_handler(
        command=ActivateDeviceCommand(device_id=device_id), session=session
    )


@router.patch("/{device_id}/deactivate", response_model=Device)
async def deactivate_device(
    device_id: uuid.UUID,
    session=Depends(get_session),
) -> Device:
    return deactivate_device_command_handler(
        command=DeactivateDeviceCommand(device_id=device_id), session=session
    )
