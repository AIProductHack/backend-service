from fastapi import APIRouter
from .schemas import User

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/create", status_code=204, response_model=User)
def create(data):
    return {200: "ok"}


@router.get("/all", status_code=200, response_model=list[User])
def all():
    return {200: "ok"}


@router.put("/update/{uuid}", status_code=200, response_model=User)
def update(uuid: str):
    return {200: "ok"}


@router.delete("/delete/{uuid}", status_code=200)
def delete(uuid: str):
    return {200: "ok"}
