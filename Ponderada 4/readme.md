# Projeto de Sistema de Logs

Esta atividade consiste na implementação de um sistema de logs para armazenar as ações que acontecem no sistema. O objetivo é utilizar um sistema de logs apresentado em sala de aula como base, conforme o material do encontro 11.

## Funcionalidades Implementadas

1. **Adição de um Gateway:** Implementação de um gateway que intermedia as requisições entre os clientes e os serviços internos.
2. **Logs do Gateway:** Inclusão de logs no gateway para registrar todas as requisições e respostas, enviando essas informações para o sistema de logs.
3. **Novo Serviço Adicional - User Services:** Criação de um serviço adicional (eventos) em Python, com funcionalidades de CRUD (Create, Read, Update, Delete) e integração de logging.
4. **Integração de Logs:** Todos os serviços, incluindo o novo serviço de eventos, estão integrados ao sistema de logs para armazenar as ações realizadas.

## Estrutura do Projeto
### Gateway
O gateway foi adicionado para controlar o fluxo de requisições entre os clientes e os serviços internos. Todas as requisições passam pelo gateway, que registra logs de cada operação.

### Sistema de Logs
Um serviço de logs foi implementado para armazenar todas as ações que acontecem no sistema. O endpoint para registrar logs é:

- URL: http://localhost:8003/log
- Método: POST
- Corpo da Requisição:

{
    "service": "string",
    "user_id": "string",
    "action": "string",
    "result": "string",
    "cause": "string",       // opcional
    "timestamp": "datetime"  // opcional, será preenchido automaticamente se não fornecido
}

### Serviço de Usuários
O serviço de usuários foi implementado utilizando FastAPI. Ele oferece endpoints para criação, leitura, atualização e exclusão de usuários. Cada ação realizada pelo serviço é registrada no sistema de logs.

Criação de Usuário: POST /users/
Leitura de Todos os Usuários: GET /users/
Leitura de um Usuário Específico: GET /users/{user_id}
Atualização de Usuário: PUT /users/{user_id}
Exclusão de Usuário: DELETE /users/{user_id}

### Logs
Cada ação nos serviços de usuários, eventos e mensageria gera um log no sistema de logs. Os logs são enviados para o endpoint /log com informações detalhadas sobre a operação realizada.

Exemplo de Log

{
    "service": "user_service",
    "user_id": "1",
    "action": "create_user",
    "result": "success",
    "timestamp": "2024-06-15T12:34:56.789Z"
}

## Execução do Projeto
Para executar o projeto, siga os passos abaixo:

- Clone o repositório do GitHub.
- Navegue até o diretório do projeto.
- Crie um ambiente virtual.
- Instale as dependências necessárias.
- Inicie os serviços de usuários.
- Inicie o gateway.
- Realize operações nos serviços e verifique os logs no sistema de logs.


### Comandos

# Clonar o repositório
git clone <https://github.com/ipatriciahonorato/modulo-10.git>

# Navegar até o diretório do projeto
cd <Ponderada 4>

# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows
venv\Scripts\activate
# No Unix ou MacOS
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar o docker-compose

docker-compose up 

# Configurar e iniciar Elastic Search
# Seguir a documentação oficial: https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html

# Configurar e iniciar Kibana
# Seguir a documentação oficial: https://www.elastic.co/guide/en/kibana/current/getting-started.html


# Vídeo Demonstrativo

O vídeo abaixo apresenta o sistema em funcionamento e os logs armazenados.

