from fastapi import FastAPI
from app.api.v1 import quotes, questions
from app.db.pool import init_db_pool

app = FastAPI(title="Diary Project API")
app.include_router(quotes.router)
app.include_router(questions.router)

@app.on_event("startup")
async def startup():
    await init_db_pool()
