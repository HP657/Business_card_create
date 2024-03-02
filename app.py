# app.py

from flask import Flask
from flask_jwt_extended import JWTManager
from routes.main import main_bp
import os

app = Flask(__name__)

# JWT 설정
app.config['JWT_SECRET_KEY'] = os.getenv("KEY")
app.config['SECRET_KEY'] = os.getenv("KEY")

# 블루프린트 등록
app.register_blueprint(main_bp)

# JWTManager 초기화
jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(debug=True)
