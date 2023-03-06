from flask_restful import Resource, reqparse
from myFlaskApi.services.user_service import UserService
from flask_jwt_extended import jwt_required


class LoginController(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("usuario", type=str, required=True)
        parser.add_argument("senha", type=str, required=True)
        args = parser.parse_args()

        usuario = args["usuario"]
        senha = args["senha"]

        return UserService.login(usuario, senha)
    
class UserController(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("usuario", type=str, required=True)
        parser.add_argument("senha", type=str, required=True)
        args = parser.parse_args()
        
        usuario = args["usuario"]
        senha = args["senha"]

        return UserService.create_user(usuario, senha)