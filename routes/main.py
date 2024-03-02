from flask import *
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from .create_card import set_card
from pool.database import DB
import os
from dotenv import load_dotenv

main_bp = Blueprint('main_bp', __name__)

load_dotenv()

# 데이터베이스 연결
db = DB(
    os.getenv("DB"),
    os.getenv("DB_USER"),
    os.getenv("DB_PW")
)

@main_bp.route('/')
def main():
    if 'token' in session:  # 세션에 토큰이 있는지 확인
        return render_template('index.html', logged_in=True)  # 로그인 상태를 템플릿에 전달
    else:
        return render_template('index.html', logged_in=False)

@main_bp.route('/signup', methods=["GET", "POST"])
def signup():
    message = None

    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        share_password = request.form['share_password']
        confirm_share_password = request.form['confirm_share_password']

        if password != confirm_password:
            message = "비밀번호가 일치하지 않습니다."
        elif share_password != confirm_share_password:
            message = "공유 비밀번호가 일치하지 않습니다."
        else:
            # 회원 가입 처리
            db.add_user(name, password, confirm_password)  # 예시: 데이터베이스에 사용자 추가
            return redirect(url_for('main_bp.main'))

    return render_template('signup.html', message=message)

@main_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = db.get_user(username, password)  # 사용자 정보 확인

    if user:
        token = create_access_token(identity=username)
        session['token'] = token  # 토큰을 세션에 저장
        return redirect(url_for('main_bp.main'))  # 메인 페이지로 리다이렉트
    else:
        flash('회원 정보가 없습니다.')
        return redirect(url_for('main_bp.main'))
    
@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main_bp.main'))

@main_bp.route('/aa')
@jwt_required()
def aa():
    encoded_image = set_card()
    return render_template('view_card.html', encoded_image=encoded_image)

@main_bp.route('/profile')
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return 'Welcome %s' % current_user
