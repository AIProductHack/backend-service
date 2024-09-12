import os
import requests
from typing import Annotated
from fastapi import (
    APIRouter,
    File,
    HTTPException,
)

ML_API = os.getenv("ML_API") + "/generation"

router = APIRouter(prefix="/query", tags=["query"])


@router.post("/text", status_code=200)
async def accept_text(text: str):
    response = requests.post(f"{ML_API}/from_text?text={text}")
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.content
        )
    return response.json()


@router.post("/audio", status_code=200)
async def accept_audio(file: Annotated[bytes, File()]):
    raise HTTPException(418, detail="Audio support is not implemented yes")


@router.post("/image", status_code=200)
async def accept_image(file: Annotated[bytes, File()]):
    raise HTTPException(418, detail="Image support is not implemented yes")
