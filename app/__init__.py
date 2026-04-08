from flask import Flask
from .models import create_tables

def create_app():
    app = Flask(__name__)
    app.secret_key = "segredo"

    from .routes import main
    app.register_blueprint(main)

    create_tables()

    return app