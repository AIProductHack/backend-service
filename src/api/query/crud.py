import os
from db.helpers import MongoHelper

db_helper = MongoHelper(os.getenv("MONGO_URL"), 'logs_service')


async def save_request(query, components, css):
    await db_helper.insert(query, components, css)
