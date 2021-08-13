from flask import Flask, request
from flask_restful import Resource, Api
from captura_de_informacoes import getTitulos

app = Flask(__name__)
api = Api(app)



class G1Titulos(Resource):
    def get(self):
        url= "https://g1.globo.com/"

        titulos = getTitulos(url)

        return geraResponse("Busca bem sucedida", "Resultado encontrado", "Titulos", titulos)

class GETitulos(Resource):
    def get(self):
        url= "https://ge.globo.com/"

        titulos = getTitulos(url)

        return geraResponse("Busca bem sucedida", "Resultado encontrado", "Titulos", titulos)



def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    response = app.make_response(response)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = '*'
    
    return response


api.add_resource(G1Titulos, '/noticias/geral')
api.add_resource(GETitulos, '/noticias/esportes')


if __name__ == '__main__':
    app.run()