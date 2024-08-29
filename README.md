# 🌐 Server-Client Flask API Real-Time

Bem-vindo ao repositório **Server-Client Flask API Real-Time**! Este projeto é uma micro aplicação prática que demonstra a criação e integração de um servidor e cliente usando **Flask**, **JWT** (JSON Web Tokens) e **SQLite**. O projeto inclui um gerador de dados que produz registros de vendas em tempo real, e o cliente consome a API para gravar dados novos e únicos em um banco SQLite.

## 🧩 **Visão Geral do Projeto**

Este projeto consiste em três componentes principais:

1. **Servidor Flask**: Um servidor que lê dados em tempo real de um arquivo JSON e fornece esses dados através de uma API RESTful.
2. **Cliente Flask**: Um cliente que consome a API do servidor, coleta dados e os grava em um banco de dados SQLite.
3. **Gerador de Dados**: Um script que gera registros de vendas e os salva em um arquivo JSON para ser consumido pelo servidor.


### 📚 **Componentes do Projeto**

#### 1. **Servidor Flask**

O servidor Flask é responsável por:

- **Autenticação**: Utiliza **JWT** para autenticar requisições e garantir a segurança na comunicação entre cliente e servidor.
- **API RESTful**: Oferece uma API que lê dados de um arquivo JSON (`data.json`) e serve esses dados em tempo real para o cliente.
- **Leitura de Dados**: O servidor lê e processa os dados em `data.json` para disponibilizá-los via API.

#### 2. **Cliente Flask**

O cliente Flask realiza as seguintes funções:

- **Consumo da API**: Conecta-se à API do servidor para obter dados.
- **Gravação no Banco de Dados**: Processa e grava registros novos e únicos em um banco de dados SQLite.
- **Autenticação JWT**: Usa JWT para autenticar as requisições feitas ao servidor, garantindo a comunicação segura.

#### 3. **Gerador de Dados**

O gerador de dados é responsável por:

- **Criação de Dados**: Gera registros de vendas e os salva em um arquivo `data.json`.
- **Atualização Contínua**: O gerador pode ser configurado para produzir dados em intervalos regulares, simulando uma fonte de dados em tempo real.

## 🛠️ **Tecnologias Utilizadas**

- **Flask**: Framework web para construir a API RESTful.
- **JWT (JSON Web Tokens)**: Utilizado para autenticação segura entre o cliente e o servidor.
- **SQLite**: Banco de dados leve e eficiente para armazenamento local dos dados pelo cliente.
- **RESTful API**: Estrutura de comunicação que permite a troca de informações entre o cliente e o servidor.

## 🚀 **Como Funciona**

1. **Configuração Inicial**:
   - **Servidor**: Inicie o servidor Flask, que estará escutando por requisições e servindo dados em tempo real.
   - **Gerador de Dados**: Execute o gerador de dados para criar o arquivo `data.json` com registros de vendas.
   - **Cliente**: Inicie o cliente Flask, que se conectará à API do servidor, consumirá os dados e gravará no banco de dados SQLite.

2. **Fluxo de Dados**:
   - O **gerador de dados** cria e atualiza o arquivo `data.json` com novos registros de vendas.
   - O **servidor Flask** lê esse arquivo e expõe os dados através de uma API RESTful.
   - O **cliente Flask** consome a API do servidor, processa os dados recebidos e os armazena em um banco de dados SQLite.

3. **Autenticação**:
   - O cliente deve autenticar suas requisições usando **JWT**, que é gerado e validado pelo servidor para assegurar a integridade e segurança das comunicações.

## 📑 **O que Este Projeto Demonstra**

- **Integração de Componentes**: Demonstra a integração entre um servidor e cliente utilizando Flask e JWT.
- **Criação de APIs RESTful**: Mostra como construir e consumir APIs RESTful com Flask.
- **Gerenciamento de Dados em Tempo Real**: Implementa um sistema que lida com dados gerados em tempo real e sua persistência em um banco de dados.
- **Segurança com JWT**: Utiliza JWT para autenticar e garantir a segurança das comunicações entre o cliente e o servidor.

## 🔗 **Links Relevantes**

- **Repositório do Projeto**: [Server_Client_Flask-API_Resltime](https://github.com/evolucaoit/Server_Client_Flask-API_Resltime)
- **Portfólio**: [Evolução IT](https://github.com/evolucaoit)
- **Outros Projetos**: [Chaos4455](https://github.com/chaos4455)
- **LinkedIn**: [Elias Andrade](https://br.linkedin.com/in/itilmgf)

---

Espero que este projeto ilustre minha capacidade de integrar e implementar soluções complexas utilizando uma stack moderna e segura. Se você tiver perguntas ou estiver interessado em colaborar, sinta-se à vontade para entrar em contato!

*Elias Andrade*

