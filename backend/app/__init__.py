from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.user_routes import user_bp
    from app.routes.notebook_routes import notebook_bp
    from app.routes.test_routes import test_bp
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(notebook_bp, url_prefix="/notebooks")
    app.register_blueprint(test_bp, url_prefix="/tests")

    with app.app_context():
        db.create_all()

    return app
