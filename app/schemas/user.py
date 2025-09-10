from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
#pydantic기반한 클라이언트의 요청(Request), 응답(Response)의 데이터 검증 스키마

class SignupRequest(BaseModel):
    phone: str
    email: EmailStr
    password: str
    nickname: str

class UserOut(BaseModel):
    id: int
    phone: str
    email: EmailStr
    nickname: str
    createDate: datetime
