from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()



@app.get("/hello")
async def hello():
    return FileResponse("index.html")

@app.get("/main.css")
async def css():
    return FileResponse("main.css")
