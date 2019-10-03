import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app
from config import Config
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager

db = MongoEngine()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    db.init_app(app)
    jwt.init_app(app)
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from app.creation import bp as creation_bp
    app.register_blueprint(creation_bp, url_prefix='/resource')
    from app.allocation import bp as allocation_bp
    app.register_blueprint(allocation_bp, url_prefix='/assign')
    return app
