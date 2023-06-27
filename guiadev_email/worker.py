#!/usr/bin/env python
import pika
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
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
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar e-mail:", str(e))
    finally:
        server.quit()
    return
    

def disparaEmail(msg):
  destinatario = 'fabio.furtado@estudante.ufla.br'
  assunto = 'Tuturial do GuiaDev'
  mensagem = msg
  remetente = REMETENTE
  senha = SENHA
  print(REMETENTE, SENHA)
  # enviar_email(destinatario, assunto, mensagem, remetente, senha)
 
 
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    disparaEmail(body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='fila', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='fila', on_message_callback=callback)
channel.start_consuming()
