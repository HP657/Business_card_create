from flask import *

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def main():
    return render_template('index.html')

@main_bp.route('/<name>')
def view_card(name):
    return send_from_directory('cards', f'{name}님의 명함.png')