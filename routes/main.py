from flask import *
from .create_card import mak_card
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
    if request.method == "POST": 
        ko_name = request.form[ko_name]
        password = request.form[password]
        share_password = request.form[share_password]
        job = request.form[job]
        en_name = request.form[en_name]
        tel = request.form[tel]
        email = request.form[email]
        img = mak_card(job, ko_name, en_name, tel, email)
        DB.add_user(ko_name, password, share_password, img)

    return render_template('index.html')

@main_bp.route("/view/<name>/<share_password>")
def view(name, share_password):
    return render_template("view.html")
    
