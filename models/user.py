from peewee import IntegerField
from models.base_model import BaseModel


class User(BaseModel):
    user_id = IntegerField()
    level = IntegerField(default=0)
