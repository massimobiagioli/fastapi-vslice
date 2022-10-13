import uuid

from pydantic import BaseModel


class DeviceBase(BaseModel):
    name: str
    address: str


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: uuid.UUID
    name: str
    address: str
    is_active: bool

    class Config:
        orm_mode = True
