# Documentação para Execução da API de Gerenciamento de Tarefas

## Pré-requisitos
Antes de iniciar, você deve ter instalado:

Python 3.8 ou superior
pip (instalador de pacotes para Python)
Configuração do Ambiente

## Clonar o Repositório
Primeiro, clone o repositório que contém o seu projeto Flask para a sua máquina local (ajuste a URL com base no URL real do seu repositório):

```
git clone https://github.com/ipatriciahonorato/modulo-10
cd Ponderada 1
```

## Instalar o Ambiente Virtual
É recomendado usar um ambiente virtual para projetos Python a fim de gerenciar as dependências de forma isolada de outros projetos Python:

```
    python3 -m venv venv
    source venv/bin/activate
```

## Instalar Dependências
Instale todos os pacotes Python necessários especificados no seu requirements.txt:

```
pip install -r requirements.txt
```

## Inicialização do Banco de Dados
Antes de executar a aplicação, certifique-se de que o banco de dados esteja inicializado para criar as tabelas necessárias:

```
python app.py create_db
```
Este comando criará um novo banco de dados SQLite chamado project.db com todas as tabelas necessárias definidas nos seus modelos.

## Executando a Aplicação Flask
Para iniciar o servidor Flask, execute:

```
python3 -m flask --app main run
```

Este comando inicia o servidor de desenvolvimento local em http://localhost:5000/. 

## Funcionalidades da API
### Usuários:
- Cadastro de Usuários: Permite o cadastro de novos usuários.
- Login: Autenticação de usuários que retorna um token JWT para acesso às funcionalidades protegidas.
- Consulta de Usuários: Permite consultar todos os usuários ou um usuário específico pelo ID.
- Atualização de Usuários: Permite atualizar dados de um usuário existente.
- Exclusão de Usuários: Permite a exclusão de um usuário pelo ID.

### Tarefas:
- Criação de Tarefas: Usuários autenticados podem criar tarefas.
- Visualização de Tarefas: Permite visualizar todas as tarefas associadas ao usuário autenticado.
- Atualização de Tarefas: Permite alterar detalhes de uma tarefa específica.
- Exclusão de Tarefas: Permite excluir uma tarefa específica.

## Insomnia Collection

### Área de trabalho
Nome: Flask App API
Descrição: Esta área de trabalho contém todos os endpoints da API definidos na aplicação Flask.
Variáveis de Ambiente
Ambiente Base: Define a variável base_url que é usada como a URL base para todas as requisições da API.
base_url - URL base da API, definida por padrão como http://localhost:5000

### Pastas e Requisições
1. Hello World
GET /: Retorna uma simples mensagem de Hello World.
2. Usuários (Pasta)
GET /users: Recupera todos os usuários.
GET /users/{user_id}: Recupera um único usuário pelo ID.
POST /users: Cria um novo usuário. Requer corpo JSON com name, email e password.
PUT /users/{user_id}: Atualiza um usuário existente identificado por ID. Requer corpo JSON com name, email e password.
DELETE /users/{user_id}: Deleta um usuário identificado por ID.
3. Autenticação (Pasta)
POST /token: Gera um token de autenticação. Requer corpo JSON com username e password.
POST /login: Simula um processo de login, gerando um token de autenticação se bem-sucedido.
POST /register: Trata do registro de usuários. Requer dados de formulário com username e password.
4. Tarefas (Pasta)
POST /tasks: Cria uma nova tarefa para o usuário autenticado. Requer corpo JSON com title e, opcionalmente, description.
GET /tasks/view: Recupera todas as tarefas associadas ao usuário autenticado.
PUT /tasks/{task_id}: Atualiza uma tarefa específica pelo ID. Requer corpo JSON com propriedades da tarefa para atualizar.
DELETE /tasks/{task_id}: Deleta uma tarefa específica pelo ID.

### Importação e Uso
Importando: Para importar esta coleção no Insomnia:
Vá até 'Dashboard'
Clique em 'Importar/Exportar'
Escolha 'Importar Dados' e depois 'De Arquivo'
Selecione o arquivo JSON onde esses dados estão salvos.
Usando Variáveis:
Certifique-se de substituir os placeholders na URL ou corpo JSON com valores reais baseados em seu cenário de teste.
Use o trocador de ambiente para mudar base_url se estiver testando em diferentes ambientes.

### Atualizando a Coleção
Para atualizar ou personalizar esta coleção, adicione ou modifique requisições ou ambientes diretamente dentro do Insomnia.



