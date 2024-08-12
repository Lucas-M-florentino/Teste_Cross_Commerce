from flask import Flask, jsonify
import random

n_routes = 100
n_floats = 100  # Número de floats por rota

app = Flask(__name__)

def generate_floats(seed, count):
    """Gera uma lista de floats aleatórios com base em uma semente."""
    random.seed(seed)
    return ["%.4f" % random.uniform(0, 100) for _ in range(count)]

@app.route('/api/<int:route_number>', methods=['GET'])
def get_floats(route_number):
    if 1 <= route_number <= n_routes:
        # Use o número da rota como semente para gerar sempre os mesmos números
        floats = generate_floats(seed=route_number, count=n_floats)
        return jsonify(floats)
    else:
        return jsonify([]), 404  # Retorna 404 se a rota não for válida

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4910)
