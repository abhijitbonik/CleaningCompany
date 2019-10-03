from flask import Flask, request
from flask_restful import Resource, reqparse
from app.models import User
from flask_jwt_extended import create_access_token, create_refresh_token

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        try:
            user = User.objects.get(username=data['username'])
        except Exception:
            return {'msg': 'User {} doesn\'t exist'.format(data['username'])}
        
        if User.verify_hash(data['password'], user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'msg': 'Logged in as {}'.format(user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'msg': 'Wrong credentials'}


