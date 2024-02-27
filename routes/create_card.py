from flask import *
from routes.PIL_def import PIL_def

create_card_bp = Blueprint('create_card_bp', __name__)

@create_card_bp.route('/create_card', methods=['POST'])
def create_card():
    직군 = request.form['직군']
    이름 = request.form['이름']
    영어이름 = request.form['영어이름']
    전화번호 = request.form['전화번호']
    PIL_def.create_card(직군, 이름, 영어이름, 전화번호)

    return '명함이 생성되었습니다.'