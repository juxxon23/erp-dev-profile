from flask import Flask
from .db.postgresql.model import db

def create_app():
    app = Flask(__name__, instance_relative_config=True) # (instance_relative_config) rutas relativas a la carpeta de la instancia, instance_path (default)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    #CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers=["Content-Type", "Authorization", "idUser"], methods=["GET", "PUT", "POST", "DELETE"], supports_credentials=True)
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,idUser')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    with app.app_context():
        from .routes import user
        add_routes(app, user)
        db.init_app(app)
        return app

def add_routes(app, user):
    # User routes
    app.add_url_rule(user['employee'], view_func=user['view_func_employee'])
    app.add_url_rule(user['allemployee'], view_func=user['view_func_allemployee'])