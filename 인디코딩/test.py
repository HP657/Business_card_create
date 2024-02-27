import psycopg2
import base64
from dotenv import load_dotenv
import os

load_dotenv()

# PostgreSQL에 연결
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password=os.getenv("DB_PW")
)

# 커서 생성
cur = conn.cursor()

# 이미지 파일을 바이너리로 읽어 Base64로 인코딩
with open('cards/ㅁ님의 명함.png', 'rb') as f:
    binary_data = f.read()
    encoded_data = base64.b64encode(binary_data).decode('utf-8')

# SQL 쿼리 실행하여 이미지 Base64 문자열 삽입
cur.execute("INSERT INTO test (img) VALUES (%s)", (encoded_data,))

# 커밋
conn.commit()

# 연결 종료
cur.close()
conn.close()
