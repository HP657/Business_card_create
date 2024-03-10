# app.py

from flask import Flask
from routes.main import main_bp
import os
from datetime import timedelta

app = Flask(__name__)

app.register_blueprint(main_bp)


if __name__ == "__main__":
    app.run(debug=True)
