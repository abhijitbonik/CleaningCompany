from app.auth import api
from app.auth.views import UserLogin, UserRegistration

api.add_resource(UserLogin, '/login')

