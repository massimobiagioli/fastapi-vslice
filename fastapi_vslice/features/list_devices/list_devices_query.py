from typing import List

from sqlalchemy.orm import Session

from fastapi_vslice.models.device import Device as DeviceModel
from fastapi_vslice.schemas.device import Device


def list_devices_query(
    session: Session
) -> List[Device]:
    return session\
        .query(DeviceModel)\
        .order_by(DeviceModel.name)\
        .all()

