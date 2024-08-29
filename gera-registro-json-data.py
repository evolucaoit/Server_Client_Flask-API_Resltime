import json
import time
from faker import Faker

# Inicialização do Faker
fake = Faker('pt_BR')

# Caminho do arquivo JSON
json_file = 'data.json'

# Função para obter o próximo ID disponível
def obter_proximo_id(dados):
    if not dados:
        return 1  # Caso o arquivo esteja vazio, começa do ID 1
    return max(item['id'] for item in dados) + 1

# Função para gerar um novo registro aleatório
def gerar_registro(proximo_id):
    return {
        "id": proximo_id,
        "nome": fake.name(),
        "email": fake.email(),
        "departamento": fake.random_element(elements=("Vendas", "Marketing", "TI", "Financeiro", "RH", "Operações", "Logística", "Compras", "Qualidade", "Desenvolvimento"))
    }

# Função para salvar o registro no arquivo JSON
def salvar_registro(novo_registro):
    try:
        with open(json_file, 'r+', encoding='utf-8') as file:
            dados = json.load(file)
            dados.append(novo_registro)
            file.seek(0)
            json.dump(dados, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump([novo_registro], file, ensure_ascii=False, indent=4)

# Função principal para adicionar um novo registro continuamente
def adicionar_registro_continuamente():
    while True:
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                dados = json.load(file)
        except FileNotFoundError:
            dados = []

        proximo_id = obter_proximo_id(dados)
        novo_registro = gerar_registro(proximo_id)
        salvar_registro(novo_registro)

        print(f"✅ Novo registro adicionado: {novo_registro['nome']} (ID: {novo_registro['id']})")
        
        # Aguarda 1 segundo antes de adicionar o próximo registro
        time.sleep(1)

# Executa a função principal
if __name__ == "__main__":
    adicionar_registro_continuamente()
