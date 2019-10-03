from flask import Blueprint
from flask_restful import Api
from app import  jwt

bp = Blueprint('allocation', __name__)
api = Api(bp)


from app.allocation import routes