from flask import Flask

from config import Config

from app.extensions import db
from app.extensions import migrate
from app.extensions import login_manager


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    # ------------------------
    # Register Blueprints
    # ------------------------

    from app.auth.routes import auth_bp
    from app.tickets.routes import ticket_bp
    from app.dashboard.routes import dashboard_bp
    from app.ai.routes import ai_bp
    from app.knowledge.routes import knowledge_bp

    app.register_blueprint(auth_bp)

    app.register_blueprint(ticket_bp)

    app.register_blueprint(dashboard_bp)

    app.register_blueprint(ai_bp)

    app.register_blueprint(knowledge_bp)

    return app