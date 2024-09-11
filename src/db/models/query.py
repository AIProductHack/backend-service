from typing import (
    TypedDict,
    Optional,
    Literal,
)
from bson.objectid import ObjectId


class Content(TypedDict):
    kind: Literal["text", "audio", "image"]
    value: str


class Query(TypedDict):
    _id: Optional[ObjectId]
    userId: Optional[ObjectId]
    content: Content
