from flask import make_response, jsonify
from poncetechApi.database.models import Estado


class EstadoService:
    
    def get_all():
        estados = Estado.query.all()

        estados_dict = [estado.to_dict() for estado in estados]

        return make_response(jsonify(estados_dict), 200)