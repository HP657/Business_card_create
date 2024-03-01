from flask import Flask
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # JWT 시크릿 키 설정
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_KEY")

    # 블루프린트 등록
    from routes.main import main_bp
    app.register_blueprint(main_bp)

    # JWTManager 초기화
    jwt = JWTManager(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
