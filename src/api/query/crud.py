import os
from db.helpers import MongoHelper
from db.models import Query

db_helper = MongoHelper(os.getenv("MONGO_URL"))


async def create_query()


