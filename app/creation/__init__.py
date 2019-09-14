from flask import Blueprint
from flask_restful import Api

bp = Blueprint('creation', __name__)
api = Api(bp)


from app.creation import routes
