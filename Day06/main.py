# from fastapi import FastAPI
# from routers.api_v1.routers import router

# description = """
# # 詳細說明
# 這邊也支援 **Markdwon**
# """

# app = FastAPI(openapi_url="")

# app.include_router(router, prefix="/api/v1")

# subapi = FastAPI()

from fastapi import FastAPI

app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


subapi = FastAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)