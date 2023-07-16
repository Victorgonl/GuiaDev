# ==================== guiadev-email ==================== #


# Criar esta imagem: docker build -t guiadev-email .
# Executar esta imagem: docker run -d --name guiadev-email --network=guiadev-network guiadev-email


# Imagem oficial do Python
FROM python

# Copiar conteúdo
COPY / /

# Requisitos pip
RUN pip install -r requirements.txt

# Execução da aplicação
CMD ["python3", "guiadev-email.py"]