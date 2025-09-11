from pydantic import BaseModel

class ReflectionQuestion(BaseModel):
    id: int
    text: str
