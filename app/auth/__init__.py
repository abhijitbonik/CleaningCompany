from flask import Blueprint
from flask_restful import Api
from app import  jwt

bp = Blueprint('auth', __name__)
api = Api(bp)
#jwt._set_error_handler_callbacks(api)

from app.auth import routes
