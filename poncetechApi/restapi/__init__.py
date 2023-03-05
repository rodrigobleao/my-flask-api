from flask import Blueprint
from flask_restful import Api

from .user_controller import LoginController, UserController
from .estado_controller import EstadoController
from .municipio_controller import MunicipioController, MunicipioEstadoController

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    app.url_map.strict_slashes = False

    api.add_resource(LoginController, "/login")
    api.add_resource(UserController, "/user")
    api.add_resource(EstadoController, "/estados")
    api.add_resource(MunicipioController, "/municipio", "/municipio/<id>")
    api.add_resource(MunicipioEstadoController, "/municipio/estado/<id_estado>")

    app.register_blueprint(bp)
