# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da API para o container
COPY . .

# Exponha a porta na qual a aplicação rodará
EXPOSE 3290

# Comando para rodar a aplicação
CMD ["python", "main.py"]
