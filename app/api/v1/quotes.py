from fastapi import APIRouter, Depends, HTTPException
from app.services.quote_service import get_random_quote, add_bookmark, get_bookmarks
from app.api.v1.deps import get_current_user, User

router = APIRouter(prefix="/quotes", tags=["quotes"])

@router.get("/random")
async def random_quote():
    return await get_random_quote()

@router.post("/{quote_id}/bookmark")
async def bookmark_quote(quote_id: int, current_user: User = Depends(get_current_user)):
    success = await add_bookmark(current_user.id, quote_id)
    if not success:
        raise HTTPException(status_code=400, detail="Already bookmarked")
    return {"msg": "Bookmarked"}

@router.get("/bookmarks")
async def my_bookmarks(current_user: User = Depends(get_current_user)):
    return await get_bookmarks(current_user.id)
