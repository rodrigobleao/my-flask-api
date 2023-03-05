from flask_restful import Resource, reqparse
from poncetechApi.services.user_service import UserService

parser = reqparse.RequestParser()
parser.add_argument("usuario", type=str, required=True)
parser.add_argument("senha", type=str, required=True)

class LoginController(Resource):
    def post(self):
        args = parser.parse_args()
        usuario = args["usuario"]
        senha = args["senha"]

        return UserService.login(usuario, senha)
    
class UserController(Resource):
    def post(self):
        args = parser.parse_args()
        usuario = args["usuario"]
        senha = args["senha"]

        return UserService.create_user(usuario, senha)