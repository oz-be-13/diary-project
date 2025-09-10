from fastapi import FastAPI
from tortoise.models import Model
from tortoise import fields

app = FastAPI()

class BlacklistToken(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="tokens")
    jwt_id = fields.CharField(max_length=255)
    expiredDate = fields.DatetimeField()
    blackDate = fields.DatetimeField(auto_now_add=True)
