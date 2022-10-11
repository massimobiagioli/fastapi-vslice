from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, String

from fastapi_vslice.database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=False)
