from flask import *
from routes.create_card import create_card_bp
from routes.main import main_bp

app = Flask(__name__)


app.register_blueprint(create_card_bp)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
