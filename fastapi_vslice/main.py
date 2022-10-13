from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from fastapi_vslice.shared.database import engine, Base
from fastapi_vslice.routers import device
from fastapi import Request

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(device.router)

templates = Jinja2Templates(directory="templates/")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
