# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Importa e registra o blueprint
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Garante que os modelos sejam carregados
    from app import models

    return app