FROM python
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY guiadev/ / guiadev/
EXPOSE 8080
# CMD ["pip", "list"]
CMD ["python3", "guiadev/manage.py", "runserver", "8080"]