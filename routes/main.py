from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from .create_card import set_card
from pool.database import DB
import os

main_bp = Blueprint('main_bp', __name__)

# 데이터베이스 연결
db = DB(
    os.getenv("DB"),
    os.getenv("DB_USER"),
    os.getenv("DB_PW")
)

# 회원 관리 함수

@main_bp.route('/')
def main():
    return render_template('index.html')

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
            db.add_user(name, password)  # 예시: 데이터베이스에 사용자 추가
            return redirect(url_for('main_bp.main'))

    return render_template('signup.html', message=message)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 사용자 인증 처리
        if db.authenticate_user(username, password):  # 예시: 사용자 인증
            access_token = create_access_token(identity=username)
            session['access_token'] = access_token
            return redirect(url_for('main_bp.profile'))

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
