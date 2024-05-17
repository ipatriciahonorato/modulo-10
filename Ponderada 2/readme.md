# Aplicativo de To-Do-List em Flutter e Flask

O projeto é composto por um serviço de backend, que gerencia as tarefas (TO-DOs), e um aplicativo móvel, que permite ao usuário interagir com essas tarefas.

## Instalação e Configuração

### Clonar o Repositório
Para obter o código do projeto, clone o repositório do GitHub abaixo.

        git clone <https://github.com/ipatriciahonorato/modulo-10.git>
	    cd <ponderada-2> (para APP Flutter)
        cd <ponderada-1> (para API Flask com Docker)
### Configuração do Ambiente Virtual
Recomenda-se a utilização de um ambiente virtual para instalar as dependências. Para criá-lo e ativá-lo:

    python3 -m venv env
    source env/bin/activate

# 1. Arquitetura da Aplicação
## 1.1 API Backend (Flask)

A API backend foi implementada em Flask. As funcionalidades incluem listar, adicionar, editar e remover tarefas. A autenticação é gerenciada via JWT (JSON Web Tokens), garantindo que apenas usuários autorizados possam acessar e modificar as tarefas.

### Endpoints da API:

- POST /token - Autenticação de usuário e retorno de um JWT.
- GET /tasks - Listagem de todas as tarefas.
- POST /tasks - Criação de uma nova tarefa.
- PUT /tasks/{task_id} - Atualização de uma tarefa existente.
- DELETE /tasks/{task_id} - Remoção de uma tarefa.

A API está presente no repositório da ponderada 1: [link](https://github.com/ipatriciahonorato/modulo-10/tree/main/Ponderada%201/Flask%20app%20(docker))

## 1.2 Aplicativo Móvel (Flutter)
O aplicativo móvel foi desenvolvido em Flutter. Ele possui as seguintes telas:

- Tela de Login - Permite ao usuário inserir credenciais e acessar o sistema.
- Tela Principal (To-Do List) - Exibe todas as tarefas, permitindo adicionar, editar e remover tarefas.

# 2.1 Tela de Login
Usuários precisam se autenticar para acessar suas tarefas. A tela de login coleta o username e a senha, e, se corretos, o sistema retorna um token JWT para acessar as demais funcionalidades.

# 2.2 Gerenciamento de Tarefas
Após o login, o usuário é direcionado para a tela principal, que lista todas as tarefas. Nesta tela, o usuário pode:

- Listar Tarefas - Todas as tarefas são listadas automaticamente ao entrar na tela principal.
- Adicionar Tarefas - Um formulário permite inserir o título e a descrição da nova tarefa.
- Editar Tarefas - Cada tarefa pode ser editada clicando sobre ela, alterando título e descrição.
- Remover Tarefas - A remoção é feita através de um long press sobre a tarefa desejada.

# 3. Container Docker para a API

A API Flask foi contêinerizada usando Docker, utilize os comandos abaixo a aplicação conforme abaixo:

```
docker build -t todo-api .
docker run -p 5000:5000 todo-api
```

# 5. Vídeo Demonstrativo

[![video demostrativo da solução](https://img.youtube.com/vi/AOzgwANrYy8/0.jpg)](https://www.youtube.com/shorts/AOzgwANrYy8)

