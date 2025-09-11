from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_token
from app.services.auth_service import AuthService
from app.models.user import User

security = HTTPBearer()
# HTTPBearer 인증 방식 설정

# 현재 요청의 사용자 정보를 확인하는 함수.
async def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)):
    token = creds.credentials
    try:
        payload = decode_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="토큰이 유효하지 않습니다.")
    jti = payload.get("jti")
    sub = payload.get("sub")

    if await AuthService.is_blacklisted(jti):
        raise HTTPException(status_code=401, detail="로그아웃된 사용자입니다.")

    #DB에서 사용자 ID로 정보 조회
    user = await User.get(id=sub)
    # 인증된 사용자 반환.
    return user
