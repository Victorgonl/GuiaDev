from enviar_email import enviar_email


# Exemplo de uso
destinatario = input("E-mail remetente: ")
assunto = 'Teste de e-mail do GuiaDev'
mensagem = 'Olá, este é um teste de e-mail do GuiaDev.'
remetente = 'guiadev2023@gmail.com'
senha = input("Senha para " + remetente + ": ")
enviar_email(destinatario, assunto, mensagem, remetente, senha)
