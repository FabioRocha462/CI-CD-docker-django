# Use uma imagem base menor
FROM python:3.11-alpine3.21

# Instale dependências do sistema necessárias para compilar mysqlclient
RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    mariadb-dev \
    pkgconfig

# Configure o diretório de trabalho
WORKDIR /app

# Copie somente os arquivos necessários para instalar as dependências
COPY requirements.txt .

# Instale as dependências no sistema
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código
COPY Docker/ .

# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Configurar o comando inicial

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]