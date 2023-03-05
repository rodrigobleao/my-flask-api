from flask import  jsonify, make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from poncetechApi.services.estado_service import EstadoService

parser = reqparse.RequestParser()

class EstadoController(Resource):
    
    @jwt_required()
    def get(self):
        return EstadoService.get_all()