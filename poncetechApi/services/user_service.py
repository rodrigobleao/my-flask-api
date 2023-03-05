from poncetechApi.database.database import db
from poncetechApi.database.models import User
from flask_jwt_extended import create_access_token
from flask import make_response, jsonify

class UserService():
    def login(usuario, senha):
        if not usuario or not senha:
            return make_response(jsonify({"message": "User or password were not provided"}), 400)
        
        user = User.query.filter_by(usuario=usuario).first()
        
        if user and user.check_password(senha):
            access_token = create_access_token(identity=user.id)

            return make_response(jsonify({"access_token": access_token}), 200)
        
        return make_response(jsonify({"message": "Access denied"}), 403)

    def create_user(usuario, senha):
        user = User(usuario=usuario, senha=senha)
        db.session.add(user)
        db.session.commit()
        
        return make_response(jsonify(user.to_dict()), 201)
