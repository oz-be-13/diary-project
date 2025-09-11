from fastapi import FastAPI
from tortoise.models import Model
from tortoise import fields

app = FastAPI()

# tortoise ORM으로 User테이블 생성.
class User(Model):
    id = fields.IntField(pk=True)
    phone = fields.CharField(max_length=11, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=255)
    nickname = fields.CharField(max_length=100)
    createDate = fields.DatetimeField(auto_now_add=True)
    modifiedDate = fields.DatetimeField(auto_now=True)

    # BlacklistToken 모델에서 user 필드와 연결됨
    tokens: fields.ReverseRelation["BlacklistToken"]
