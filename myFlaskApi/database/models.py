from myFlaskApi.database.database import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash, generate_password_hash


class Estado(db.Model, SerializerMixin):
    __tablename__ = "estados"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32),unique=True, nullable=False)
    sigla = db.Column(db.String(2),unique=True, nullable=False)


class Municipio(db.Model, SerializerMixin):
    __tablename__ = "municipios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128),unique=True, nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey("estados.id"), nullable=False)


class User(db.Model, SerializerMixin):
    serialize_rules = ("-_senha",)
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(128),unique=True, nullable=False)
    _senha = db.Column("senha", db.String(128), nullable=False)

    @hybrid_property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = generate_password_hash(senha)
    
    def check_password(self, senha):
        return check_password_hash(self._senha, senha)
    
    