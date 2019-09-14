from flask import Flask, request
from flask_restful import Resource
from app.models import db, Employee

class ListCreateEmployeeApi(Resource):
    def get(self):
        return Employee.objects().to_json()

    def post(self):
        email = request.json['email']
        fname = request.json['fname']
        lname = request.json['lname']
        dob = request.json['dob']
        identity = request.json['id']
        phone = request.json['phone']
        emp=Employee(email=email, first_name=fname, last_name=lname, dob=dob, identification=identity, phone=phone)
        emp.save()
        return emp.to_json()


