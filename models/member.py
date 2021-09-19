from peewee import IntegerField
from models.base_model import BaseModel


class Member(BaseModel):
    user_id = IntegerField()
    server_id = IntegerField()
    level = IntegerField(default=0)
