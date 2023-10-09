from fastapi import FastAPI
from log import init_logging
import logging

app = FastAPI()

logger = init_logging()

logger_ac = logging.getLogger("uvicorn.access")
logger_ac.handlers = []

@app.get("/")
async def root():
    logger.info("Logger Info")
    logger.error("Logger Error")
    print("Hi")
    return {"message": "Hello World"}