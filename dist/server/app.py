from flask import Flask, jsonify, request
from flask_cors import CORS

import logging
import uuid

logging.basicConfig(level=logging.DEBUG)

PROJETOS = [
    {
        "id": uuid.uuid4().hex,
        "Título": "Residência Moderna",
        "Imagem": "residencia_moderna.jpg",
        "Área": 250,
        "Descrição": "Uma residência moderna com espaços integrados e design minimalista.",
        "Visivel": True
    },
    {
        "id": uuid.uuid4().hex,
        "Título": "Escritório Corporativo",
        "Imagem": "escritorio_corporativo.jpg",
        "Área": 500,
        "Descrição": "Projeto de um escritório corporativo com áreas colaborativas e tecnologia de ponta.",
        "Visivel": False
    },
    {
        "id": uuid.uuid4().hex,
        "Título": "Casa de Campo",
        "Imagem": "casa_de_campo.jpg",
        "Área": 300,
        "Descrição": "Casa de campo com design rústico e aconchegante, cercada por natureza.",
        "Visivel": True
    }
]


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/projetos', methods=['GET', 'POST'])
def all_projects():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        try:
            post_data = request.get_json()
            if not post_data:
                logging.error("No JSON data received")
            else:
                logging.debug(f"Received data: {post_data}")

            PROJETOS.append({
                'id': uuid.uuid4().hex,
                'Título': post_data.get('Título'),
                'Imagem': post_data.get('Imagem'),
                'Área': post_data.get('Área'),
                'Descrição': post_data.get('Descrição'),
                'Visivel': post_data.get('Visivel')
            })
            response_object['message'] = 'Projeto adicionado!'
        except Exception as e:
            response_object['status'] = 'error'
            response_object['message'] = str(e)
    else:
        response_object['projetos'] = PROJETOS
    return jsonify(response_object)

@app.route('/projetos/<projeto_id>', methods=['PUT'])
def single_project(projeto_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_project(projeto_id)
        PROJETOS.append({
            'id': uuid.uuid4().hex,
            'Título': post_data.get('Título'),
            'Imagem': post_data.get('Imagem'),
            'Área': post_data.get('Área'),
            'Descrição': post_data.get('Descrição'),
            'Visivel': post_data.get('Visivel')
        })
        response_object['message'] = 'Projeto updated!'
    return jsonify(response_object)


def remove_project(projeto_id):
    for projeto in PROJETOS:
        if projeto['id'] == projeto_id:
            PROJETOS.remove(projeto)
            return True
    return False

if __name__ == '__main__':
    app.run(port=5001)