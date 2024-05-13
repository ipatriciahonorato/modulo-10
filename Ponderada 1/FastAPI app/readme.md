# API Síncrona feita em FastApi - Acesso a Página secreta

## Pré-requisitos
Antes de iniciar, certifique-se de ter instalado:

- Python 3.8 ou superior
- Docker e Docker Compose

## Clonar o repositório

```
git clone https://github.com/ipatriciahonorato/modulo-10
cd Ponderada 1
```

## Docker
Utilize o Docker para configurar e iniciar todos os serviços necessários:

```
docker-compose up --build
```

Este comando construirá as imagens necessárias e iniciará os contêineres definidos no Docker Compose, incluindo a API e o banco de dados.

## Estrutura do Projeto

Este projeto consiste em duas APIs principais:

- API Flask (Assíncrona): A primeira versão da API, implementada em Flask, manipula autenticações e operações de usuário básicas. (Pasta: [link](https://github.com/ipatriciahonorato/modulo-10/tree/main/Ponderada%201/Checkpoint%20-%20P1%20-%2002))
- API FastAPI (Síncrona): A segunda versão, reescrita em FastAPI, oferece melhor desempenho e é utilizada para operações relacionadas ao gerenciamento de dispensadores de medicamentos. (Presente nessa pasta)

## Banco de Dados

A configuração do banco de dados foi atualizada para usar um serviço de banco de dados mais robusto, substituindo o SQLite por uma solução adequada ao ambiente de produção (ajuste a descrição conforme o banco de dados específico utilizado).

## Executando a Aplicação FastAPI
Após iniciar os serviços com Docker, a API estará disponível em:

URL da API FastAPI: http://localhost:8000/

## Funcionalidades da API FastAPI

### Usuários:
- Cadastro de Usuários: Permite o cadastro de novos usuários.
- Login: Autenticação de usuários que retorna um token JWT para acesso às funcionalidades protegidas.
- Acesso de página protegida.

## Uso do Insomnia
Para testar a API, você pode importar a coleção de requisições para o Insomnia. Certifique-se de configurar as variáveis de ambiente necessárias para apontar para os URLs corretos da API.
