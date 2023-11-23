import smtplib

def enviar_email(destinatario, mensagem): 
    remetente = "seu_email@gmail.com"
    senha = "sua_senha"

    assunto = "Assunto do e-mail"

    mensagem_formatada = f"Assunto: {assunto}\n\n{mensagem}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(remetente, senha)
    server.sendmail(remetente, destinatario, mensagem_formatada)

# Lista dos e-mails para enviar
destinatarios = ["email@example.com", "email2@example.com", "email3@example.com"]

# Mensagem para ser enviada
mensagem = "Olá, você se cadastrou com sucesso!"

# Esse e o envio
for destinatario in destinatarios:
    enviar_email(destinatario, mensagem)