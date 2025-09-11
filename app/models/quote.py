from pydantic import BaseModel

class Quote(BaseModel):
    id: int
    text: str
    author: str

class QuoteBookmark(BaseModel):
    user_id: int
    quote_id: int

