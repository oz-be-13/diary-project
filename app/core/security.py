import uuid
import jwt
from passlib.context import CryptContext # 비밀번호 해싱 및 검증
from datetime import datetime, timedelta
from app.core.config import settings # 환경 변수 (JWT 시크릿, 알고리즘, 만료시간 등)

# 비밀번호 해싱에 bcrypt 알고리즘을 사용할 것.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    #사용자의 비밀번호를 해싱하여 안전하게 저장한다.
    return pwd_context.hash(password)

def verify_password(raw: str, hashed: str) -> bool:
    #사용자가 입력한 비밀번호(raw)와 DB에 저장된 해시값을 비교하여 검증한다.
    return pwd_context.verify(raw, hashed)

#JWT 액세스 토큰 생성 함수
def create_access_token(user_id: int) -> tuple[str, str, datetime]:
    # 고유 식별자(jti) 생성 → 블랙리스트 처리 등에 사용
    jti = uuid.uuid4().hex
    # 토큰 만료 시간 설정 (현재 시간 + 설정된 유효 시간)
    expire = datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRE)
    # JWT에 담을 정보 구성
    payload = {
        "sub": str(user_id),  # 사용자 ID
        "jti": jti,           # 토큰 고유 ID
        "exp": expire         # 토큰 만료 시간
    }

    # JWT 토큰 생성
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGO)

    # 토큰, jti, 만료시간을 튜플로 반환
    return token, jti, expire

def decode_token(token: str) -> dict:
    #JWT 토큰을 디코딩하여 payload(내부 정보)를 추출
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGO])
