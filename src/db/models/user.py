from typing import TypedDict, NotRequired
from bson.objectid import ObjectId


class User(TypedDict):
    _id: NotRequired[ObjectId]
    username: str
    password: str
