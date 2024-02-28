from flask import *
from pool.database import DB
import os

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

@main_bp.route('/login')
def login():
    pass

@main_bp.route('/<name>')
def view_card(name):
    return send_from_directory('cards', f'{name}님의 명함.png')