from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import SignupRequest, UserOut              # 회원가입 요청 및 사용자 응답 스키마
from app.schemas.auth import LoginRequest, TokenResponse         # 로그인 요청 및 토큰 응답 스키마
from app.services.auth_service import AuthService                # 인증 서비스 호출
from app.core.deps import get_current_user, security             # 인증 토큰 검증 및 사용자 추출 함수

# 인증 관련 라우터 생성
router = APIRouter(prefix="/auth", tags=["auth"])

# 회원가입 엔드포인트
@router.post("/signup", response_model=UserOut)
async def signup(data: SignupRequest):
    try:
        # AuthService를 통해 회원가입 처리
        user = await AuthService.signup(data)
        return user
    except ValueError as e:
        # 오류 발생 시 400 Bad Request 반환
        raise HTTPException(status_code=400, detail=str(e))

# 로그인 엔드포인트
@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest):
    try:
        # 이메일과 비밀번호로 로그인 시도, JWT 토큰 반환
        token, _, _, _ = await AuthService.login(data.email, data.password)
        return TokenResponse(access_token=token)
    except ValueError as e:
        # 오류 시 401 Unauthorized 반환
        raise HTTPException(status_code=401, detail=str(e))

# 로그아웃 엔드포인트
@router.post("/logout")
async def logout(creds=Depends(security)):
    try:
        # 토큰 추출 후 블랙리스트 등록
        await AuthService.logout(creds.credentials)
        return {"detail": "로그아웃 완료"}
    except ValueError as e:
        # 토큰 디코딩 실패 등 오류 시 400 Bad Request 반환
        raise HTTPException(status_code=400, detail=str(e))

#️ 현재 로그인된 사용자 정보 조회
@router.get("/me", response_model=UserOut)
async def me(user=Depends(get_current_user)):
    # get_current_user()를 통해 인증된 사용자 객체 추출
    return user
