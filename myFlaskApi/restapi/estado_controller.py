from flask_restful import Resource
from flask_jwt_extended import jwt_required

from myFlaskApi.services.estado_service import EstadoService

class EstadoController(Resource):
    
    def get(self):
        return EstadoService.get_all()