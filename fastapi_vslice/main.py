import uuid

from fastapi import FastAPI, Depends

from fastapi_vslice.crud.device import create_device
from fastapi_vslice.database import engine, Base, get_session
from fastapi_vslice.schemas.device import DeviceCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/test")
async def test_create(device: DeviceCreate, session=Depends(get_session)):
    create_device(
        session=session,
        device=device
    )

    return {"message": "new device created"}
