# Usar uma imagem base oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho no container para corresponder à sua estrutura
WORKDIR /app

# Copiar o arquivo de dependências e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o diretório src para o diretório de trabalho
COPY src/ .

# O diretório de instâncias pode ser omitido se você estiver usando o Postgres
# COPY instance/ instance/

# Copiar o diretório templates
COPY src/ templates

# Definir variáveis de ambiente (ajuste conforme necessário)
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV DATABASE_URL=postgresql://username:password@db:5432/mydatabase
ENV JWT_SECRET_KEY=goku-vs-vegeta

# Expôr a porta 5000 para acesso externo ao container
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["flask", "run", "--host=0.0.0.0"]



