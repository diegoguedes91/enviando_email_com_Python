from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'meu_email@gmail.com' # insira aqui o seu email
minha_senha = 'Abc@123' # insira aqui sua senha

with open('template.html', 'r') as html:
    template = Template(html.read())
    dataatual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Diego', data = dataatual)

# configurando a composição do envio do email
msg = MIMEMultipart()
msg['from'] = 'Diego Guedes'
msg['to'] = 'email_do_cliente@email.com' #insira o email da pessoa que vai receber o seu email
msg['subject'] = 'Atenção: este é um email de testes.'

# inserindo o template na mensagem do email
corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# anexando a imagem
with open('snoopy.jpg', 'rb') as jpg:
    jpg = MIMEImage(jpg.read())
    msg.attach(jpg)

# configurando o email gmail
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('Email enviado com sucesso!')
    except Exception as e:
        print('Email não enviado...')
        print('Erro: ', e)
