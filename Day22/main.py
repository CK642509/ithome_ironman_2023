from fastapi import FastAPI, Request
# from log import logger, init_logger
from logger import init_logging
from loguru import logger
import logging

app = FastAPI()

init_logging()

@app.get("/")
async def root(request: Request):
    logger.info("loguru info log")
    logging.info("logging info log")

    logging.getLogger("fastapi").debug("fatapi info log")
    logger.bind(payload=dict(request.query_params)).debug("params with formating")

    
    print("Hi")
    return {"message": "Hello World"}