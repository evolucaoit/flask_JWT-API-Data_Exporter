from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime
import json
import logging

app = Flask(__name__)
CORS(app)  # Habilita CORS
app.config['SECRET_KEY'] = '123'

# Configuração de logs
logging.basicConfig(filename='server.log', level=logging.INFO)

def authenticate(username, password):
    """Função para autenticar o usuário com base no login.json."""
    try:
        with open('login.json') as f:
            users = json.load(f)
        return users.get(username) == password
    except Exception as e:
        logging.error(f'Error in authenticate function: {e}')
        return False

def token_required(f):
    """Decorador para verificar se o token JWT está presente e é válido."""
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorator

@app.route('/login', methods=['POST'])
def login():
    """Rota para autenticação e emissão de token JWT."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if authenticate(username, password):
        token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                           app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/data/<int:id>', methods=['GET'])
@token_required
def get_data(id):
    """Rota para retornar dados de transações bancárias com base no ID."""
    try:
        with open('data.json') as f:
            data = json.load(f)
        result = [item for item in data if item['id'] == id]
        return jsonify(result)
    except Exception as e:
        logging.error(f'Error in get_data function: {e}')
        return jsonify({'message': 'Error loading data!'}), 500

if __name__ == '__main__':
    app.run(port=666)
