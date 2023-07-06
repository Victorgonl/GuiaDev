#!/usr/bin/env python
import os
import pika
import time
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

REMETENTE = os.getenv('REMETENTE')
SENHA = os.getenv('SENHA')


def enviar_email(destinatario, assunto, mensagem, remetente, senha):
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587

    msg = MIMEMultipart()
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    msg.attach(MIMEText(mensagem, "plain"))

    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        print()
        print("From:", msg['From'])
        print("To:", msg['To'])
        print("Subject:", msg['Subject'])
        print()
        print(mensagem)
        print("===========================")
        print("E-mail enviado com sucesso!")
        print("===========================")
        print()
    except Exception as e:
        print(destinatario, assunto, mensagem, remetente)
        print("Erro ao enviar e-mail:", str(e))
    finally:
        server.quit()
    return


def disparaEmail(msg):
    destinatario = msg['destinatario']
    assunto = "Tutorial do GuiaDev: " + msg['titulo'] + " by " + msg["autor"]
    conteudos = ""
    for conteudo in msg['conteudos']:
        conteudos += conteudo + "\n"
    mensagem = msg['titulo'] + "\n"
    mensagem += "by: " + msg['autor'] + '\n\n'
    mensagem += msg['descricao'] + '\n\n'
    mensagem += conteudos
    remetente = REMETENTE
    senha = SENHA
    enviar_email(destinatario, assunto, mensagem, remetente, senha)


def callback(ch, method, properties, body):

    msg = json.loads(body.decode())
    disparaEmail(msg)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.18.0.2',port=5672, credentials=credentials)) #Docker
# connection = pika.BlockingConnection(
 #    pika.ConnectionParameters(host='0.0.0.0', credentials=credentials)) #local
channel = connection.channel()
channel.queue_declare(queue='fila', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='fila', on_message_callback=callback)
channel.start_consuming()


