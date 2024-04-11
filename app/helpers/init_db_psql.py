from flask import Flask
from app.db.postgresql.model import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://grim:pass1234test@localhost/dberp'
    with app.app_context():
        db.init_app(app)
        db.create_all()