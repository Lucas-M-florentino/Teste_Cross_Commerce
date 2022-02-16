import json
from flask import Flask, jsonify
from os import path, walk

apiRest = Flask(__name__)

@apiRest.route('/')
def index():
    txt = ''
    with open('index.html','r') as f:
        txt = f.read()
    dados = ''
    for i in txt:
        dados = dados + i
        
    return txt

if __name__ == "__main__":
    apiRest.run(debug=True)
    