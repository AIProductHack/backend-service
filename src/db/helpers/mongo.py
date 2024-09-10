from typing import Any
from pymongo import MongoClient


class MongoHelper:
    def __init__(self, host: str, db: str) -> None:
        self.db = MongoClient(host)[db]

    def find(self, collection: str, params: dict[str, Any]):
        result = [item for item in self.db[collection].find(params)]
        return result

    def write(self, collection: str, data: dict[str, Any]):
        self.db[collection].insert_one(data)
