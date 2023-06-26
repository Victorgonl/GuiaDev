FROM python
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY guiadev/ / guiadev/
# CMD ["pip", "install", "-r", "requirements.txt"]
# CMD ["pip", "list"]
# comandos para reiniciar os serviços de rede e reiniciar o docker caso dê erro ao rodar pip install:
# systemctl restart NetworkManager.service
# sudo service docker restart
CMD ["python3", "guiadev/manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000