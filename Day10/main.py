from fastapi import FastAPI
from config import Settings
from fastapi.middleware.cors import CORSMiddleware

from fastapi.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response
    
middleware = [
    Middleware(CustomHeaderMiddleware)
]

app = FastAPI(middleware=middleware)

settings = Settings()

# @app.middleware()

# app.add_middleware(CORSMiddleware)

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }