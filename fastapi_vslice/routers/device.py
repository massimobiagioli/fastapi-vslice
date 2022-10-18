import uuid

from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from fastapi_vslice.features.activate_device.activate_device_command import activate_device_command_handler, \
    ActivateDeviceCommand
from fastapi_vslice.features.create_device.create_device_command import create_device_command_handler, \
    CreateDeviceCommand
from fastapi_vslice.features.create_device.create_device_form import CreateDeviceForm
from fastapi_vslice.features.deactivate_device.deactivate_device_command import deactivate_device_command_handler, \
    DeactivateDeviceCommand
from fastapi_vslice.features.list_devices.list_devices_query import list_devices_query
from fastapi_vslice.schemas.device import DeviceCreate
from fastapi_vslice.shared.database import get_session

router = APIRouter(
    prefix="/devices",
)

templates = Jinja2Templates(directory="fastapi_vslice/")


@router.get("/list", response_class=HTMLResponse)
async def list_devices(
        request: Request,
        session=Depends(get_session)
):
    devices = list_devices_query(session=session)
    return templates.TemplateResponse(
        name="features/list_devices/list_devices.html",
        context={
            "request": request,
            "devices": devices
        }
    )


@router.get("/new", response_class=HTMLResponse)
async def new_device(request: Request):
    return templates.TemplateResponse(
        name="features/create_device/create_device.html",
        context={"request": request}
    )


@router.post("/new", response_class=HTMLResponse)
async def new_device(
        request: Request,
        session=Depends(get_session)
):
    form = CreateDeviceForm(request=request)
    await form.load_data()
    if not form.validate():
        return templates.TemplateResponse(
            name="features/create_device/create_device.html",
            context={"request": request, "errors": form.errors}
        )
    created_device = create_device_command_handler(
        command=CreateDeviceCommand(
            device_id=uuid.uuid4(),
            payload=DeviceCreate(**form.__dict__)
        ),
        session=session
    )

    return templates.TemplateResponse(
        name="features/create_device/create_device.html",
        context={"request": request, "created_device_id": created_device.id}
    )


@router.get("/{device_id}/activate", response_class=HTMLResponse)
async def activate_device(
        device_id: uuid.UUID,
        request: Request
):
    return templates.TemplateResponse(
        name="features/activate_device/activate_device.html",
        context={"request": request, "device_id": device_id}
    )


@router.post("/{device_id}/activate", response_class=HTMLResponse)
async def activate_device(
        device_id: uuid.UUID,
        request: Request,
        session=Depends(get_session)
):
    device = activate_device_command_handler(
        command=ActivateDeviceCommand(
            device_id=device_id
        ),
        session=session
    )
    return templates.TemplateResponse(
        name="features/activate_device/activate_device.html",
        context={
            "request": request,
            "device_id": device_id,
            "device_activated": device.is_active
        }
    )


@router.get("/{device_id}/deactivate", response_class=HTMLResponse)
async def deactivate_device(
        device_id: uuid.UUID,
        request: Request
):
    return templates.TemplateResponse(
        name="features/deactivate_device/deactivate_device.html",
        context={"request": request, "device_id": device_id}
    )


@router.post("/{device_id}/deactivate", response_class=HTMLResponse)
async def deactivate_device(
        device_id: uuid.UUID,
        request: Request,
        session=Depends(get_session)
):
    device = deactivate_device_command_handler(
        command=DeactivateDeviceCommand(
            device_id=device_id
        ),
        session=session
    )
    return templates.TemplateResponse(
        name="features/deactivate_device/deactivate_device.html",
        context={
            "request": request,
            "device_id": device_id,
            "device_deactivated": device.is_active is False
        }
    )
