from flask import Flask
from flask_cors import CORS
from .db.postgresql.model import db

def create_app():
    app = Flask(__name__, instance_relative_config=True) # (instance_relative_config) rutas relativas a la carpeta de la instancia, instance_path (default)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    CORS(app, support_credentials=True)
    
    with app.app_context():
        from .routes import user
        add_routes(app, user)
        db.init_app(app)
        return app

def add_routes(app, user):
    # User routes
    app.add_url_rule(user['employee'], view_func=user['view_func_employee'])