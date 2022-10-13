from fastapi import FastAPI

from fastapi_vslice.shared.database import engine, Base
from fastapi_vslice.routers import device

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(device.router)


@app.get("/")
async def home():
    return {"message": "Hello World"}
