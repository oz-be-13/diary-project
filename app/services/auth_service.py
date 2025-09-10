from tortoise.exceptions import DoesNotExist
from app.models.user import User
from app.models.blacklist_token import BlacklistToken
from app.core.security import hash_password, verify_password, create_access_token, decode_token
from datetime import datetime

# 회원 가입과 로그인 서비스 클래스.
class AuthService:
    @staticmethod
    async def signup(data):
        #회원가입 : 이메일 중복 여부 확인, 비밀번호 해싱 후 사용자 생성
        exists = await User.filter(email=data.email).exists()
        if exists:
            raise ValueError("이미 존재하는 이메일입니다.")
        user = await User.create(
            phone=data.phone,
            email=data.email,
            password=hash_password(data.password),
            nickname=data.nickname
        )
        return user

    @staticmethod
    async def login(email: str, password: str):
        #로그인 처리 : 이메일로 사용자 조회, 비밀번호 검증, JWT 토큰 생성 및 반환
        try:
            user = await User.get(email=email)
        except DoesNotExist:
            raise ValueError("존재하지 않는 사용자입니다.")
        if not verify_password(password, user.password):
            raise ValueError("비밀번호가 올바르지 않습니다.")
        token, jti, exp = create_access_token(user.id)
        return token, jti, exp, user

    @staticmethod
    async def logout(token: str):
        #로그아웃 : 토큰 디코딩 후 jti 추출, 해당 토큰을 블랙리스트에 등록
        payload = decode_token(token)
        jti = payload.get("jti")
        exp = payload.get("exp")
        sub = payload.get("sub")
        if not jti or not exp:
            raise ValueError("유효하지 않은 토큰입니다.")
        await BlacklistToken.create(
            user_id=int(sub),
            jwt_id=jti,
            expiredDate=datetime.fromtimestamp(exp)
        )

    @staticmethod
    async def is_blacklisted(jti: str) -> bool:
        #해당 토큰 jti가 블랙리스트에 있는 지 확인. 있으면 True(만료됨) 없으면 False(유효함), bool값 반환.
        return await BlacklistToken.filter(jwt_id=jti).exists()
