from fastapi import APIRouter

router = APIRouter()

@router.get("", summary="summmary")
async def get_data():
    """
    # Markdwon
    ## Hello World

    Cool!
    - I can write markdwon message here
    - It's **awesome**
    """
    return {"message": "Hello World"}

@router.post("")
async def root():
    return {"message": "Hello World"}