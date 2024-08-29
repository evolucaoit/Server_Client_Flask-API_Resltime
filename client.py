import requests
import sqlite3
import time
import logging
import sys

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuração do banco de dados SQLite
db_file = 'data.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id TEXT PRIMARY KEY,
    nome TEXT,
    email TEXT,
    departamento TEXT
)
''')
conn.commit()

# Função para verificar se o ID já existe no banco de dados
def id_exists(id):
    cursor.execute('SELECT 1 FROM usuarios WHERE id = ?', (id,))
    return cursor.fetchone() is not None

# Função para inserir usuário no banco de dados
def insert_user(user):
    cursor.execute('INSERT INTO usuarios (id, nome, email, departamento) VALUES (?, ?, ?, ?)',
                   (user['id'], user['nome'], user['email'], user['departamento']))
    conn.commit()
    logging.info(f"🟢 Usuário inserido: {user['nome']}")

# Função para autenticação e obtenção do token JWT
def authenticate(auth_url, login_payload):
    try:
        response = requests.post(auth_url, json=login_payload)
        response.raise_for_status()
        return response.json().get('access_token')
    except requests.exceptions.RequestException as e:
        logging.error(f'🔴 Falha na autenticação: {e}')
        sys.exit(1)

# Função principal para buscar dados continuamente
def fetch_data_continuously(data_url, headers):
    backoff_time = 1  # Tempo inicial de backoff em segundos

    while True:
        try:
            response = requests.get(data_url, headers=headers)
            response.raise_for_status()

            users = response.json()
            for user in users:
                if not id_exists(user['id']):
                    insert_user(user)
            backoff_time = 1  # Reseta o backoff após uma resposta bem-sucedida
        except requests.exceptions.RequestException as e:
            logging.error(f'🔴 Erro ao acessar dados: {e}')
            backoff_time = min(backoff_time * 2, 60)  # Aumenta o backoff exponencialmente até um máximo de 60 segundos
        
        logging.info(f"⏳ Aguardando {backoff_time} segundos antes da próxima tentativa...")
        time.sleep(backoff_time)

# Configurações da API
auth_url = 'http://localhost:777/login'
data_url = 'http://localhost:777/data'

login_payload = {
    'username': 'admin',
    'password': '1234'
}

# Autenticação
token = authenticate(auth_url, login_payload)
if token:
    headers = {'Authorization': f'Bearer {token}'}
    logging.info('🟢 Autenticado com sucesso.')

    # Iniciar busca de dados continuamente
    fetch_data_continuously(data_url, headers)

# Fechar conexão com o banco de dados ao finalizar
conn.close()
