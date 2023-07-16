# ==================== guiadev ==================== #


# Criar esta imagem: docker build -t guiadev .
# Executar esta imagem: docker run -d --name guiadev --network=guiadev-network -p 8000:8000 guiadev
# Acessar GuiaDev: http://localhost:8000/


# Imagem oficial do Python
FROM python

# Copiar conteúdo
COPY / /

# Pporta
EXPOSE 8000

# Requisitos pip
RUN pip install -r requirements.txt

# Execução do servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]