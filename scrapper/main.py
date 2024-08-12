from flask import Flask
from views.views import web_view

app = Flask(__name__)

# Registra o blueprint das rotas
app.register_blueprint(web_view)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3290)
