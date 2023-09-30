from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/assets", StaticFiles(directory="dist/assets"))

templates = Jinja2Templates(directory="dist")

@app.get("/")
async def read_item(request: Request):
    # return templates.TemplateResponse("index.html", {"request": request})
    return FileResponse("dist/index.html")
