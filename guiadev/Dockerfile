FROM python
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY manage.py /manage.py
CMD ["python", "manage.py", "runserver"]