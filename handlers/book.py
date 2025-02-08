from fastapi import APIRouter


router = APIRouter(prefix='book', tags=['book'])


@router.get("/")
def get_task():
    return {"Hello": "World"}


@router.post("/task_id")
def post_task():
    return {"Hello": "World"}