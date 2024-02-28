from flask import *
from routes.PIL_def import PIL_def

create_card_bp = Blueprint('create_card_bp', __name__)

@create_card_bp.route('/create_card', methods=['POST'])
def create_card():
    이름 = request.form['이름']
    card = PIL_def.set_card(이름)
    