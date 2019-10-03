from flask import Flask, request
from flask_restful import Resource, reqparse
from app.models import User
from flask_jwt_extended import create_access_token, create_refresh_token

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)
parser.add_argument('email', help = 'This field cannot be blank')

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

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        try:
            User.objects.get(username=data['username'])
            return {'msg': 'User {} already exist'.format(data['username'])}
        except User.DoesNotExist:
            pass
        
        new_user = User(
            email = data['email'],
            username = data['username'],
            password = User.generate_hash(data['password'])
        )
        
        try:
            new_user.save()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'msg': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'msg': 'Something went wrong'}, 500

