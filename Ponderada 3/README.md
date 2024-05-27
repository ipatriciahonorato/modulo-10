# Projeto de Remoção de Background de Imagens e Serviço de Notificação

Este projeto consiste em um aplicativo Flutter que permite aos usuários remover o fundo de imagens e agendar notificações locais. O processamento das imagens é realizado por uma API Flask que aplica técnicas de manipulação de imagens utilizando a biblioteca Pillow. Além disso, o projeto está containerizado utilizando Docker.

# Instalação

## Backend - API Flask

1. Clone o repositório:

``
    git clone <https://github.com/ipatriciahonorato/modulo-10.git>
    cd <ponderada 3\backend>
``

2. Construa a imagem Docker:

``
docker build -t flask-backend .
``

3. Execute o container Docker:

``
docker run -d -p 5000:5000 flask-backend
``
![logs](../Ponderada%203/imgs/docker.png)

## Frontend (App Flutter)

1. Navegue até o repositório:

``
    cd <ponderada 3\encontro08>
``

2. Instale as dependências:

``
flutter pub get
``

3. Execute o aplicativo no main.dart

``
flutter run
``

# Configuração

## API Flask

Certifique-se de que o arquivo app.py está configurado corretamente para aceitar solicitações e processar imagens. Altere o endereço IP e a porta conforme necessário.

``
final uri = Uri.parse('http://192.168.15.156:5000/process-image');  // Atualize para o endereço IP correto
``

## App Flutter

Atualize a URL da API no arquivo remove_background.dart para apontar para o endereço IP correto onde o backend Flask está sendo executado.

# Usos Gerais

## App Flutter

- Abra o aplicativo Flutter.
- Selecione uma imagem da galeria.
- O aplicativo enviará a imagem para o servidor Flask para processamento.
- A imagem processada será exibida no aplicativo.
- O usuário pode salvar a imagem processada no armazenamento local.
- Para agendar notificações locais, vá para a tela de agendamento, insira o tempo em segundos e pressione o botão para criar a notificação.

# API Flask
A API Flask possui os seguintes endpoints:

    POST /token
    
    Descrição: Verifica as credenciais do usuário e retorna um token JWT.
    
    Parâmetros:
    
    username (json): Nome de usuário.
    
    password (json): Senha.
    
    Resposta: Token JWT.
    
    POST /register
    
      
    
    Descrição: Registra um novo usuário.
    
    Parâmetros:
    
    username (form-data): Nome de usuário.
    
    password (form-data): Senha.
    
    Resposta: Mensagem de sucesso ou erro.
    
    POST /process-image
    
      
    
    Descrição: Recebe uma imagem e retorna a imagem com o fundo removido.
    
    Parâmetros:
    
    image (file): Imagem a ser processada.
    
    Resposta: Imagem processada no formato PNG.

# Logs
O backend utiliza a biblioteca logging para registrar eventos importantes e facilitar a depuração. O arquivo de configuração de logs está localizado em ``backend/logs/logger.py``.

![logs](../Ponderada%203/imgs/logs.png)

# Controller e Serviços

## Controller
O controller principal do projeto está localizado em ``backend/controllers/main_controller.py`` e é responsável por definir os endpoints da API e integrar os serviços. Ele inclui endpoints para registro de usuários, autenticação e processamento de imagens.

## Serviços
Os serviços são responsáveis pela lógica de negócio e estão localizados no diretório backend/services/. Existem dois serviços principais:

``image_service.py:`` Contém a lógica para processamento de imagens, incluindo a remoção do fundo.

``user_service.py:`` Gerencia a lógica de autenticação e registro de usuários.

# Demonstração

O vídeo abaixo apresenta a demonstração do projeto desenvolvido.

[![video demostrativo da solução](https://i3.ytimg.com/vi/o9Kcp8vYQ0s/maxresdefault.jpg)](https://youtu.be/o9Kcp8vYQ0s)