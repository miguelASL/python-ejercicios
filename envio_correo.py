import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mi_correo = 'hola@gmail.com'
mi_password = 'password'
destinatario = 'prueba@gmail.com'
message = MIMEMultipart()
message['From'] = mi_correo
message['To'] = destinatario
message['Subject'] = 'Asunto del correo'

body = 'Hola, este es un correo de prueba'
message.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(mi_correo, mi_password)
text = message.as_string()
server.sendmail(mi_correo, destinatario, text)
server.quit()
print('Correo enviado')

def enviar_correo(mi_correo, mi_password, destinatario, asunto, cuerpo):
    message = MIMEMultipart()
    message['From'] = mi_correo
    message['To'] = destinatario
    message['Subject'] = asunto
    message.attach(MIMEText(cuerpo, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mi_correo, mi_password)
    text = message.as_string()
    server.sendmail(mi_correo, destinatario, text)
    server.quit()
    print('Correo enviado')

# Ejemplo de uso
enviar_correo('hola@gmail.com', 'password', 'prueba@gmail.com', 'Asunto del correo', 'Hola, este es un correo de prueba')