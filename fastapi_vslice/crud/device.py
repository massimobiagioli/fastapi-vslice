import uuid

from sqlalchemy.orm import Session

from fastapi_vslice.models.device import Device as DeviceModel
from fastapi_vslice.schemas.device import DeviceCreate


# Move into features
def create_device(session: Session, device: DeviceCreate):
    new_device = DeviceModel(
        id=str(uuid.uuid4()),
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
