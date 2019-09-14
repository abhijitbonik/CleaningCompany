from app.auth import api
from app.auth.views import Login, Logout

api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

