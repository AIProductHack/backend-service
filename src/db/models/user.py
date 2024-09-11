from typing import TypedDict, Optional
from bson.objectid import ObjectId


class User(TypedDict):
    _id: Optional[ObjectId]
    username: str
    password: str
