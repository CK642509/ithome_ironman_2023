from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
from typing import Any, Dict, Union

app = FastAPI()

class NewHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: Any = None, headers: Union[Dict[str, Any], None] = None, msg: str = None) -> None:
        super().__init__(status_code, detail, headers)
        # frontend only gets detail
        # msg is for logging
        # if no msg, system will log detail
        if msg:
            self.msg = msg
        else:
            self.msg = detail

@app.middleware("http")
async def get_request(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:     # 非預期的錯誤
        print("Error:", e)     # 紀錄非預期的錯誤的 log
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"},
        )

@app.exception_handler(NewHTTPException)
async def unicorn_exception_handler(request: Request, exc: NewHTTPException):
    print("Error:", exc.detail)   # 紀錄可預期的錯誤的 log
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.get("/")
async def hello():
    try:
        print(a)
        b = 1 / 0
    except NameError as e:   # 可預期的錯誤
        raise NewHTTPException(status.HTTP_501_NOT_IMPLEMENTED, detail="This is Value Error")