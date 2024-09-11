from pymongo import MongoClient
from pymongo.collection import Collection


class MongoHelper:
    def __init__(self, host: str, db: str) -> None:
        self.db = MongoClient(host)[db]

    def get_collection(self, collection: str) -> Collection:
        return self.db[collection]
