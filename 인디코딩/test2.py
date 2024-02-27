from flask import Flask, render_template, Response
import psycopg2
import base64
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# PostgreSQL 연결 정보
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password= os.getenv("DB_PW")
)

def fetch_image_from_database():
    # PostgreSQL 커넥션과 커서 생성
    cur = conn.cursor()

    # 이미지 데이터를 불러오는 SQL 쿼리 실행
    cur.execute("SELECT img FROM test;")
    
    # 이미지 데이터 읽기
    image_data = cur.fetchone()[0]

    # 커서와 커넥션 닫기
    cur.close()

    # Base64 디코딩
    decoded_data = base64.b64decode(image_data)
    
    return decoded_data

@app.route('/')
def index():
    # 이미지 데이터를 불러오는 함수 호출
    image_data = fetch_image_from_database()

    # 이미지를 Base64로 인코딩하여 HTML에 포함
    encoded_image = base64.b64encode(image_data).decode('utf-8')

    # HTML 템플릿 렌더링
    return render_template('index1.html', encoded_image=encoded_image)

if __name__ == '__main__':
    app.run(debug=True)
