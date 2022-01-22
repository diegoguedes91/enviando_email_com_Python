# Curso de Python 3 do Básico ao Avançado 
#### Desafio: Script de envio de email em Python utilizando template HTML

O Script deve ter um template de corpo de email e anexar uma imagem para o envio de email. 


#### Template simples criado em HTML: 
```html 
<!doctype html>
<html>
<head>

</head>
<body>
    <p>Olá $nome, hoje é $data.</p>

</body>
</html>
```

## Script: 

As variaveis _meu_email_ e _minha_senha_ devem ser inseridas o email e senha do remetente.  

```python
from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'meu_email@gmail.com' # insira aqui o seu email
minha_senha = 'Abc@123' # insira aqui sua senha
```

O Python abrira o template e substituira o _$nome_ e _$data_ do arquivo HTML salvando em _corpo_msg_. 

```python
with open('template.html', 'r') as html:
    template = Template(html.read())
    dataatual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Diego', data = dataatual)
```

Abaixo são as configurações de composição de envio de email, inserindo o template na mensagem e anexando uma imagem. </br>
Basta substituir estas informações para utilizar este script.

```python
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
```

Conforme o codigo abaixo, este script esta confirado apenas paro o gmail, caso precise utilizar outros provedores de email altere o codigo de acordo com as informações do seu provedor.
```python
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
```

Caso tenha problemas de autenticação de email mesmo com o user e senha corretos entre no link abaixo:

[https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps)

Ative a opção *Permitir aplicativos menos seguros* conforme a imagem abaixo.

![ativar opção de app no gmail](https://github.com/diegoguedes91/enviando_email_com_Python/blob/main/ativar_app.JPG)


## EMAIL: 

![imagem do email enviado](https://github.com/diegoguedes91/enviando_email_com_Python/blob/main/email.JPG)
