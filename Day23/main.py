# main.py
from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from logger import init_logging, logger
from handle import NewHTTPException
app = FastAPI()

init_logging()

@app.middleware("http")
async def get_request(request: Request, call_next):
    try:
        response = await call_next(request)
        if response.status_code < 400:
            logger.info("Info")
        return response
    except Exception as e:     # 非預期的錯誤   
        logger.error(e)        # 紀錄非預期的錯誤的 log
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"},
        )

@app.exception_handler(NewHTTPException)
async def unicorn_exception_handler(request: Request, exc: NewHTTPException):
    logger.error(exc.msg)           # 紀錄可預期的錯誤的 log
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.get("/")
async def hello():
    # b = 1 / 0
    try:
        print(a)
    except NameError as e:   # 可預期的錯誤
        raise NewHTTPException(status.HTTP_501_NOT_IMPLEMENTED, detail="This is Value Error", msg=str(e))
    print("Hi")
    return {"message": "Hello World"}