from pydantic import BaseModel
#로그인 시도시, 데이터와 토큰을 검증하는 스키마.

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"