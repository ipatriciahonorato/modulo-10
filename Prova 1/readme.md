# Prova 1

## Nome: Patricia Honorato Moreira

# Descrição 

Este projeto consiste na implementação de uma API RESTful utilizando Flask, que permite o cadastro, visualização, edição e exclusão de pedidos. A API atende ao nível de maturidade 2 do Modelo de Maturidade de Richardson e foi testada utilizando collections do Insomnia. A solução também foi dockerizada para facilitar a implantação e execução.

## Funcionalidades

- Cadastro de Pedidos: Permite cadastrar um novo pedido fornecendo nome, e-mail e descrição.
- Visualização de Pedidos: Permite visualizar todos os pedidos cadastrados.
- Visualização de Pedido por ID: Permite visualizar um pedido específico utilizando seu ID.
- Edição de Pedidos: Permite editar os detalhes de um pedido específico utilizando seu ID.
- Exclusão de Pedidos: Permite excluir um pedido específico utilizando seu ID.

# Endpoints da API

```json
1. Cadastro de Novo Pedido

Rota: /novo
Método: POST
Descrição: Cadastra um novo pedido.
Request Body:
{
  "name": "Nome do Usuário",
  "email": "email@exemplo.com",
  "description": "Descrição do pedido"
}

Resposta de Sucesso:
{
  "id": 1
}

2. Retornar Todos os Pedidos
Rota: /pedidos
Método: GET
Descrição: Retorna todos os pedidos cadastrados.
Resposta de Sucesso:

[
  {
    "id": 1,
    "name": "Nome do Usuário",
    "email": "email@exemplo.com",
    "description": "Descrição do pedido"
  }
]

3. Retornar um Pedido Específico por ID
Rota: /pedidos/{id}
Método: GET
Descrição: Retorna os dados de um pedido específico pelo ID.
Resposta de Sucesso:

{
  "id": 1,
  "name": "Nome do Usuário",
  "email": "email@exemplo.com",
  "description": "Descrição do pedido"
}

Resposta de Erro:
{
  "error": "Order not found"
}

4. Editar um Pedido Específico por ID
Rota: /pedidos/{id}
Método: PUT
Descrição: Atualiza os dados de um pedido específico pelo ID.
Request Body:
{
  "name": "Nome Atualizado",
  "email": "email_atualizado@exemplo.com",
  "description": "Descrição atualizada do pedido"
}

Resposta de Sucesso:
{
  "id": 1,
  "name": "Nome Atualizado",
  "email": "email_atualizado@exemplo.com",
  "description": "Descrição atualizada do pedido"
}
Resposta de Erro:

{
  "error": "Order not found"
}

5. Excluir um Pedido Específico por ID
Rota: /pedidos/{id}
Método: DELETE
Descrição: Exclui um pedido específico pelo ID.
Resposta de Sucesso:
{
  "message": "Order deleted successfully"
}

Resposta de Erro:

{
  "error": "Order not found"
}
```

# Testes Insomnia

A API foi testada utilizando collections do Insomnia. Para realizar os testes basta importar o arquivo de collection json no Insomnia, com o servidor funcionando será possível testar todas as rotas.

# Inicialização com Docker

## Instalação e Configuração

### Clonar o Repositório
Para obter o código do projeto, clone o repositório do GitHub abaixo.
```
        git clone <https://github.com/ipatriciahonorato/modulo-10.git>
	    cd <prova 1> 
```

### Configuração do Ambiente Virtual
Recomenda-se a utilização de um ambiente virtual para instalar as dependências. Para criá-lo e ativá-lo:
```
    python3 -m venv env
    source env/bin/activate
```

## Construa a imagem Docker:
```
docker-compose build
```

## Inicie os serviços:

```
PORT=5001 docker-compose up
```
Acesse a API através da URL: http://localhost:5001
