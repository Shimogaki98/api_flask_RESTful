from flask import request
from flask_restful import Resource
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']


class Habilidade(Resource):
    def get(self, id):
        return lista_habilidades[id]

    def delete(self, id):
        lista_habilidades.pop(id)
        return lista_habilidades


class ListaHabilidades(Resource):
    def post(self):
        dados = json.loads(request.data)
        if (dados in lista_habilidades):
            return 'habilidade já cadastrada: ' + f'{dados}'
        else:
            lista_habilidades.append(dados)
            return lista_habilidades

    def get(self):
        return lista_habilidades
