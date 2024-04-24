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

### Testando a API com Insomnia

