from app.creation import api
from app.creation.views import ListCreateEmployeeApi

api.add_resource(ListCreateEmployeeApi, '/employee/get_or_create')
