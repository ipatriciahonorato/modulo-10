# Documentação para Execução da API em Flask (Assíncrona) - Gerenciamento de Tarefas

## Pré-requisitos
Antes de iniciar, certifique-se de ter instalado:

- Python 3.8 ou superior
- Docker e Docker Compose

## Clonar o Repositório
Clone o repositório que contém o projeto da API:

```
git clone https://github.com/ipatriciahonorato/modulo-10
cd Checkpoint - P1 - 02
```

## Docker
Utilize o Docker para configurar e iniciar todos os serviços necessários:

```
docker-compose up --build
```

Este comando construirá as imagens necessárias e iniciará os contêineres definidos no Docker Compose, incluindo a API e o banco de dados.


## Funcionalidades da API

### Autenticação:
- Login: Autentica um usuário e retorna um cookie com um token JWT.
- Registro: Registra um novo usuário no sistema.

### Usuários:
- Criação de Usuários: Permite cadastrar novos usuários.
- Consulta de Usuários: Lista todos os usuários ou detalha um usuário específico pelo ID.
- Atualização de Usuários: Atualiza informações de um usuário existente.
- Exclusão de Usuários: Remove um usuário pelo ID.

### Tarefas:
- Criação de Tarefas: Permite que usuários autenticados adicionem novas tarefas.
- Visualização de Tarefas: Exibe todas as tarefas associadas ao usuário autenticado.
- Atualização de Tarefas: Modifica detalhes de uma tarefa específica.
- Exclusão de Tarefas: Apaga uma tarefa específica.

## Banco de Dados
O sistema utiliza uma conexão configurada via variável de ambiente. Em desenvolvimento, utiliza SQLite como fallback. 

## Uso no Insomnia

Para testar a API:

Para testar a API, você pode importar a coleção de requisições para o Insomnia. Certifique-se de configurar as variáveis de ambiente necessárias para apontar para os URLs corretos da API.

