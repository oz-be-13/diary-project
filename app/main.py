# app/main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api.v1 import auth
from app.core.config import settings

load_dotenv()  # .env 로드

def get_async_dsn() -> str:

    dsn = os.getenv("DATABASE_URL_ASYNC")
    if dsn:
        if dsn.startswith("postgresql+asyncpg://"):
            dsn = "postgres://" + dsn.split("://", 1)[1]
        return dsn

    required = ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        raise RuntimeError(
            "Missing env vars for DB. Provide DATABASE_URL_ASYNC or all of: "
            + ", ".join(missing)
        )

    host = os.environ["DB_HOST"]
    port = os.environ["DB_PORT"]
    name = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    pwd  = os.environ["DB_PASSWORD"]
    return f"postgres://{user}:{pwd}@{host}:{port}/{name}"

app = FastAPI()
app.include_router(auth.router, prefix="/api/v1")

register_tortoise(
    app,
    db_url=get_async_dsn(),
    modules={"models": ["app.models.user", "app.models.blacklist_token"]},
    generate_schemas=True,
    add_exception_handlers=True,
)