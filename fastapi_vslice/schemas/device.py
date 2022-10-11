import uuid

from pydantic import BaseModel


class Device(BaseModel):
    id: uuid.UUID
    name: str
    address: str
    is_active: bool

    class Config:
        orm_mode = True
