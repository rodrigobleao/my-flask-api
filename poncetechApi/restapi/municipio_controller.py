from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from poncetechApi.services.municipio_service import MunicipioService

parser = reqparse.RequestParser()
parser.add_argument("id_estado", type=int, required=True)
parser.add_argument("nome", type=str, required=True)
parser.add_argument("id", type=str, required=True)

class MunicipioController(Resource):
    def post(self):
        args = parser.parse_args()
        id_estado = str(args["id_estado"])
        nome = str(args["nome"])

        return MunicipioService.create(id_estado, nome)
    
    def get(self):
        return MunicipioService.get_all()

    def put(self):
        args = parser.parse_args()
        id = str(args["id"])
        nome = str(args["nome"])

        return MunicipioService.update(id, nome)
    
    def delete(self, id):
        return MunicipioService.delete(id)
    

class MunicipioEstadoController(Resource):
        parser.add_argument("id_estado", type=int)

        def get(self, id_estado):

            return MunicipioService.get_by_relationship(id_estado)
    