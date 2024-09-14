import os
import requests
from typing import Annotated
from fastapi import (
    APIRouter,
    File,
    HTTPException,
)

from api.query.crud import save_request
from api.query.utils import parse_css, add_styles

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
    result = response.json()
    # try:
    # css = parse_css(result['css'])
    # add_styles(result['data'], css)
    # except Exception as e:
    # print(e)
    await save_request(text, result['data'], result['css'])
    return result


@router.post("/audio", status_code=200)
async def accept_audio(file: Annotated[bytes, File()]):
    raise HTTPException(418, detail="Audio support is not implemented yet")


@router.post("/image", status_code=200)
async def accept_image(file: Annotated[bytes, File()]):
    raise HTTPException(418, detail="Image support is not implemented yet")
