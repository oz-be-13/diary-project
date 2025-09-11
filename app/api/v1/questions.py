from fastapi import APIRouter
from app.services.quote_service import get_random_question

router = APIRouter(prefix="/questions", tags=["questions"])

@router.get("/random")
async def random_question():
    return await get_random_question()
