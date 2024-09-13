from pydantic import BaseModel


class QueryScheme(BaseModel):
    user_id: str
