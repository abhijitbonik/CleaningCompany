from app.auth import api
from app.auth.views import UserLogin

api.add_resource(UserLogin, '/login')

