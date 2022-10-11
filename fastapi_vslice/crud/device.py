import uuid

from sqlalchemy.orm import Session

from fastapi_vslice.models.device import Device as DeviceModel
from fastapi_vslice.schemas.device import Device as DeviceSchema


# Move into features
def create_device(session: Session, device: DeviceSchema):
    new_device = DeviceModel(
        id=str(device.id),
        name=device.name,
        address=device.address,
        is_active=device.is_active,
    )
    session.add(new_device)
    session.commit()
    session.refresh(new_device)
    return new_device


def get_device(session: Session, device_id: uuid):
    return session.query(DeviceModel).filter(DeviceModel.id == device_id).first()
