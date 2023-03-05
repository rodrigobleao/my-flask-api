from flask import jsonify, make_response
from poncetechApi.database.database import db
from poncetechApi.database.models import Municipio


class MunicipioService():
    def create(id_estado, nome):
        municipio = Municipio(nome=nome, estado_id=id_estado)

        db.session.add(municipio)
        db.session.commit()

        return make_response(jsonify(municipio.to_dict()), 201)

    def get_all():
        municipios = Municipio.query.all()

        municipios_dict = [municipio.to_dict() for municipio in municipios]

        return make_response(jsonify(municipios_dict), 200)

    def get_by_relationship(estado_id):
        municipios = Municipio.query.filter_by(estado_id = estado_id).all()

        municipios_dict = [municipio.to_dict() for municipio in municipios]

        return make_response(jsonify(municipios_dict), 200)

    def update(id, nome):
        municipio = Municipio.query.filter(Municipio.id == id).first()
        
        if municipio and municipio.id and nome:
            municipio.nome = nome
            db.session.commit()

            return make_response(jsonify(municipio.to_dict()), 200)
        
        elif(not nome):
            return make_response(jsonify({"error": "No content provided for update."}), 400)
            
        return make_response(jsonify({"error": "No content found"}), 404)

    def delete(id):
        municipio = Municipio.query.filter(Municipio.id == id).first()
        
        if not municipio:
            return make_response(jsonify({"error": "No content found with id provided"}), 404)

        db.session.delete(municipio)
        db.session.commit()

        return make_response(jsonify({"message": "Deleted with success"}), 200)
        