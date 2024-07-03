from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from .logging import configure_logging

db = SQLAlchemy()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    configure_logging(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "ML Clustering Service"})
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    with app.app_context():
        from .routes import main_routes, api_routes
        app.register_blueprint(main_routes.bp)
        app.register_blueprint(api_routes.bp)
        
        return app
