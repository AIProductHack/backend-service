from typing import Annotated
from fastapi import APIRouter, File

router = APIRouter(prefix="/query", tags=["query"])


@router.post("/text", status_code=200)
def accept_text(text: str):
    return {200: "ok"}


@router.post("/audio", status_code=200)
def accept_audio(file: Annotated[bytes, File()]):
    return {200: "ok"}


@router.post("/image", status_code=200)
def accept_image(file: Annotated[bytes, File()]):
    return {200: "ok"}

