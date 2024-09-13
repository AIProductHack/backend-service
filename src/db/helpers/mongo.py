from pymongo import MongoClient
import uuid
from datetime import datetime


class MongoHelper:
    def __init__(self, host: str, db: str) -> None:
        self.db = MongoClient(host)[db]
        self.request_response_col = self.db['request_response_collection']

    def insert(self, query, components, css):
        item = {
            '_id': uuid.uuid4(),
            'adding_time': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'user_query': query,
            'generated_components': components,
            'generated_css': css
        }
        self.request_response_col.insert_one(item)
