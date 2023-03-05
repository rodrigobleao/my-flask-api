import click
from poncetechApi.database.database import db
from poncetechApi.services.user_service import UserService
from poncetechApi.database.models import Estado


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""

    estados_brasileiros = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins',
    }

    data = []

    for idx, (sigla, nome) in enumerate(estados_brasileiros.items()):
        estado = Estado(sigla=sigla, nome=nome)
        data.append(estado)

    db.session.bulk_save_objects(data)
    db.session.commit()
    return Estado.query.all()


def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    @app.cli.command()
    @click.option('--usuario', '-u')
    @click.option('--senha', '-p')
    def add_user(usuario, senha):
        """Adds a new user to the database"""
        return UserService.create_user(usuario, senha)
