import os

# 환경 변수에서 데이터베이스 설정 읽기
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),  # 기본값: localhost
    "user": os.getenv("DB_USER", "root"),      # 기본값: root
    "password": os.getenv("DB_PASSWORD", ""),  # 기본값: 빈 문자열
    "database": os.getenv("DB_NAME", "test"),  # 기본값: test
}