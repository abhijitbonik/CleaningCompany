from app.creation import api
from app.creation.views import WorkerApi, VehicleApi, EquipmentApi, JobApi


api.add_resource(WorkerApi, '/employees', '/employee/<string:id>')
api.add_resource(VehicleApi, '/vehicles', '/vehicle/<string:id>')
api.add_resource(EquipmentApi, '/equipments', '/equipment/<string:id>')
api.add_resource(JobApi, '/jobs', '/job/<string:id>')

