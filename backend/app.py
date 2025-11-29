from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Usando variável de ambiente para mostrar o nome do serviço
    container_name = os.environ.get('CONTAINER_NAME', 'unknown')
    return f'Resposta do container: {container_name}'

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)