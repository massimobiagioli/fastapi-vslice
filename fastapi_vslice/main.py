from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from fastapi_vslice.shared.database import engine, Base
from fastapi_vslice.routers import device

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(device.router)

templates = Jinja2Templates(directory="fastapi_vslice/")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        name="templates/home.html",
        context={"request": request}
    )
