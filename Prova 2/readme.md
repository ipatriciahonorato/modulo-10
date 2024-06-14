# Prova 2

Este projeto é uma API simples de blog construída com FastAPI, servida usando Uvicorn e NGINX como proxy reverso. A API permite a criação, leitura, atualização e exclusão (CRUD) de postagens de blog. O projeto é containerizado utilizando Docker e Docker Compose.

## Nome: Patricia Honorato Moreira

## Tecnologias Utilizadas

- FastAPI
- Uvicorn
- NGINX
- Docker
- Docker Compose

## Configuração

1. Clone o repositório:

git clone <URL_do_repositorio>
cd <nome_do_diretorio_do_projeto>

2. Criação do ambiente virtual:

python -m venv venv

venv\Scripts\activate

3. Instalação das dependências:

pip install -r requirements.txt


## Estrutura do Projeto

PROVA 2/
├── app/
│   ├── main.py
├── requirements.txt
├── Dockerfile
├── Dockerfile.nginx
├── nginx.conf
└── docker-compose.yml

## Instruções para Execução

1. Inicialização do docker:

docker-compose up --build

2. Acesso a aplicação:

Abra o navegador web e vá para http://localhost

## Testando com Insomnia

- Importe o arquivo insomnia.json no aplicativo do Insomnia e teste as rotas. 
- Para executar os testes selecione o workspace "FastAPI Blog".
- Certifique-se de que a URL base está configurada para http://localhost.
- deactivExecute as solicitações para testar os endpoints da API.





