from flask import Flask, request
from flask_restful import Resource


class Login(Resource):
    def get(self):
        return 'success login'

class Logout(Resource):
    def get(self):
        return 'success logout'


