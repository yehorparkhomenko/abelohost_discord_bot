from peewee import *

from .settings import db


class BaseModel(Model):
    class Meta:
        database = db
