FROM python
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY guiadev/ / guiadev/
# CMD ["pip", "list"]
CMD ["python3", "guiadev/manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000