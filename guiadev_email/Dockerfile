FROM python
COPY requirements.txt /requirements.txt
COPY worker.py /worker.py
RUN pip install -r requirements.txt

CMD ["python3", "worker.py"]