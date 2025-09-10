import os
from dotenv import load_dotenv

load_dotenv()

#JWT 환경설정.

class Settings:
    JWT_SECRET = os.getenv("JWT_SECRET_KEY", "secret")
    JWT_ALGO = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRE = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "3600"))

#설정 값을 변수에 담아 반환.
settings = Settings()
