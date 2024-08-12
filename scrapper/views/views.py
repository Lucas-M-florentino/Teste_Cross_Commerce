from flask import Blueprint, jsonify, request
import json
import math

web_view = Blueprint('web_view', __name__)

@web_view.route('/numeros', methods=['GET'])
def exibir_numeros():
    pagina = request.args.get('pagina', 1, type=int)  # Pega o número da página a partir dos parâmetros da URL
    tamanho_pagina = 10  # Defina quantos números você deseja exibir por página

    try:
        with open('database/numeros_ordenados.json', 'r') as f:
            numeros = json.load(f)
    except FileNotFoundError:
        return jsonify({"error": "Arquivo de números não encontrado"}), 404

    # Calcula os limites para a paginação
    inicio = (pagina - 1) * tamanho_pagina
    fim = inicio + tamanho_pagina
    total_paginas = math.ceil(len(numeros) / tamanho_pagina)

    numeros_pagina = numeros[inicio:fim]

    return jsonify({
        "pagina": pagina,
        "total_paginas": total_paginas,
        "numeros": numeros_pagina
    })
