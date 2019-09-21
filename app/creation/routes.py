from app.creation import api
from app.creation.views import WorkerApi, VehicleApi, EquipmentApi


api.add_resource(WorkerApi, '/employee', '/employee/<string:id>')
api.add_resource(VehicleApi, '/vehicle', '/vehicle/<string:id>')
api.add_resource(EquipmentApi, '/equipment', '/equipment/<string:id>')

