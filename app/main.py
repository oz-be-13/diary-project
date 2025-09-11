from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api.v1 import auth
from app.core.config import settings

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1")

register_tortoise(
    app,
    db_url="postgres://user:password@localhost:5432/dbname",
    modules={"models": ["app.models.user", "app.models.blacklist_token"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
