# app/api/v1/deps.py
from fastapi import Depends, HTTPException
from app.models.user import User  # User 모델 위치에 따라 경로 조정
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # JWT 토큰 검증 로직
    # 예시: 실제 DB 조회 및 User 반환
    user = User(id=1, username="testuser")
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user
