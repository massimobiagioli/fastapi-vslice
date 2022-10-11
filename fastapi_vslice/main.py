import uuid

from fastapi import FastAPI, Depends

from fastapi_vslice.crud.device import create_device
from fastapi_vslice.database import engine, Base, get_session
from fastapi_vslice.schemas.device import Device

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def main_route(session=Depends(get_session)):
    device = Device(id=uuid.uuid4(), name="test", address="10.10.10.11", is_active=False)
    create_device(session, device)

    return {"message": "Hello World"}
