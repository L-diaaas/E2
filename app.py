from flask import Flask
from config import Config 
from alunos.alunos_rotas import alunos_blueprint 


app = Flask(__name__)


app.config.from_object(Config)


app.register_blueprint(alunos_blueprint)


if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
