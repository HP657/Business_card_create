from flask import *
from pool.database import DB
import os
from .create_card import set_card

from dotenv import load_dotenv

load_dotenv()


main_bp = Blueprint('main_bp', __name__)


db = DB(
    os.getenv("DB"),
    os.getenv("DB_USER"),
    os.getenv("DB_PW")
)


@main_bp.route('/')
def main():
    return render_template('index.html')


@main_bp.route('/signupa', methods=["GET", "POST"])
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
            # 여기서 회원가입 로직을 처리할 수 있습니다.
            print(name, password, confirm_password, share_password, confirm_share_password)
            return redirect(url_for('main_bp.main'))

    return render_template('signup.html', message=message)


@main_bp.route('/login')
def login():
    pass

@main_bp.route('/aa')
def aa():
    encoded_image = set_card()
    return render_template('view_card.html', encoded_image=encoded_image)