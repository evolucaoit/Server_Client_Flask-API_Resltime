from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import json
import threading
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = '123'  # Chave secreta para o JWT
jwt = JWTManager(app)

data = []
data_file_path = os.path.abspath('data.json')

login_data = {}
login_file_path = os.path.abspath('login.json')

# Função para carregar os dados dos arquivos JSON
def load_data():
    global data, login_data
    try:
        with open(data_file_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

    try:
        with open(login_file_path, 'r') as f:
            login_data = json.load(f)
    except Exception as e:
        print(f"Erro ao carregar dados de login: {e}")

# Função que roda em uma thread para monitorar o arquivo JSON
class DataChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == data_file_path:
            print("Arquivo data.json modificado.")
            load_data()

def monitor_file_changes():
    event_handler = DataChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(data_file_path), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Iniciar a thread para monitorar alterações no arquivo JSON
threading.Thread(target=monitor_file_changes, daemon=True).start()

# Rota para autenticação
@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        username = request.json.get('username')
        password = request.json.get('password')
        if username == login_data.get('username') and password == login_data.get('password'):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Credenciais inválidas"}), 401

# Rota protegida para acessar os dados
@app.route('/data', methods=['GET'])
@jwt_required()
def get_data():
    return jsonify(data), 200

if __name__ == '__main__':
    load_data()  # Carregar os dados inicialmente
    app.run(port=777)
