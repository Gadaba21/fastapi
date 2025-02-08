from fastapi import APIRouter

router = APIRouter(prefix='ping', tags=['ping'])


@router.get("/")
def read_root():
    return {"Hello": "World"}
