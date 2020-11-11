from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidade, ListaHabilidades, lista_habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Marcello',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Bronzatti',
        'habilidades': ['Python', 'Django']
    }
]

# devolve um dev por ID, também altera e deleta um registro de dev
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe'.format(id)
            response = {'status': 'Erro', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'erro desconhecido, procure o administrador da API'
            response = {'status': 'Erro', 'Mensagem': mensagem}
        return response

    # permite alterar as habilidades de um dev, se a habilidade informada constar na lista de habilidades
    def put(self, id):
        dados = json.loads(request.data)
        skills = []
        for d in dados['habilidades']:
            if (d in lista_habilidades):
                print(f'{d} está na lista de habilidades')
                skills.append(d)
            else:
                print(f'{d} não está na lista de habilidades')
        desenvolvedores[id]['habilidades'] = skills
        return desenvolvedores[id]

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluido'}


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

api.add_resource(Habilidade, '/skills/<int:id>/')
api.add_resource(ListaHabilidades, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)
