from flask import Flask, request
from flask_restful import Resource
from app.models import db, Worker, Vehicle, Equipment

class WorkerApi(Resource):
    def get(self, id=None):
        if id:
            worker = self.get_worker(id)
            return worker.to_json() if worker else  {'status' : 'Worker not found'}
        return Worker.objects().to_json()

    def post(self):
        if request.is_json:
            email = request.json['email']
            fname = request.json['fname']
            lname = request.json['lname']
            dob = request.json['dob']
            identity = request.json['identity']
            phone = request.json['phone']
            worker=Worker(email=email, first_name=fname, last_name=lname, dob=dob, identification=identity, phone=phone, availibility=True)
            worker.save()
            return worker.to_json()
        return {'status': 'invalid request'}

    def put(self, id):
        return task, 201

    def delete(self, id):
        if id:
            worker = self.get_worker(id)
            if worker:
                worker.delete()
                return {'status': 204, 'message': 'worker successfully deleted'}
            return  {'status' : 404, 'message': 'worker not found'}
        return {'status' : 404 , 'message': 'invalid request'}

    def get_worker(self, id):
        try:
            return Worker.objects.get(identification=id)
        except Worker.DoesNotExist:
            return None


class VehicleApi(Resource):
    def get(self, id=None):
        if id:
            vehicle = self.get_vehicle(id)
            return vehicle.to_json() if vehicle else  {'status' : 'Vehicle not found'}
        return Vehicle.objects().to_json()

    def post(self):
        if request.is_json:
            name = request.json['name']
            seats = request.json['seats']
            uid = request.json['uid']
            vehicle=Vehicle(name=name, seats=seats, uid=uid, availibility=True)
            vehicle.save()
            return vehicle.to_json()
        return {'status': 'invalid request'}

    def put(self, id):
        return '', 201

    def delete(self, id):
        if id:
            vehicle = self.get_vehicle(id)
            if vehicle:
                vehicle.delete()
                return {'status': 204, 'message': 'vehicle successfully deleted'}
            return  {'status' : 404, 'message': 'vehicle not found'}
        return {'status' : 404 , 'message': 'invalid request'}

    def get_vehicle(self, id):
        try:
            return Vehicle.objects.get(uid=id)
        except Vehicle.DoesNotExist:
            return None


class EquipmentApi(Resource):
    def get(self, id=None):
        if id:
            equp = self.get_equipment(id)
            return equp.to_json() if equp else  {'status' : 'Equipment not found'}
        return Equipment.objects().to_json()

    def post(self):
        if request.is_json:
            uid = request.json['uid']
            etype = request.json['etype']
            brand = request.json['brand']
            model = request.json['model']
            remarks = request.json['remarks']
            equp=Equipment(uid=uid, etype=etype, brand=brand, model=model, remarks=remarks, availibility=True)
            equp.save()
            return equp.to_json()
        return {'status': 'invalid request'}

    def delete(self, id):
        if id:
            equp = self.get_equipment(id)
            if equp:
                equp.delete()
                return {'status': 204, 'message': 'Equipment successfully deleted'}
            return  {'status' : 404, 'message': 'Equipment not found'}
        return {'status' : 404 , 'message': 'invalid request'}

    def put(self, id):
        return '', 201

    def get_equipment(self, id):
        try:
            return Equipment.objects.get(uid=id)
        except Equipment.DoesNotExist:
            return None