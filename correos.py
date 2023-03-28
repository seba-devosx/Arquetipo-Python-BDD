import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sebastianignaaravenasandoval@gmail.com'
smtp_password = "stwczzlkbohustcz"

# Lista de destinatarios
msg = MIMEMultipart()
to_addresses = ['sebastianigna98@icloud.com', 'sebastianignaaravenasandoval@gmail.com']
msg['Bcc'] = ", ".join(to_addresses)
# Crear el objeto de mensaje multipart
msg['From'] = smtp_username
#msg['To'] = ', '.join(addres_ocult)
msg['Subject'] = 'Correo enviado desde python'

# Cuerpo del correo electrónico
body = 'Este es un mensaje de prueba enviado desde python'

# Agregar el cuerpo del mensaje al objeto MIMEText
msg.attach(MIMEText(body, 'plain'))

# Iniciar sesión en el servidor SMTP
smtp_server = smtplib.SMTP(smtp_server, smtp_port)
smtp_server.starttls()
smtp_server.login(smtp_username, smtp_password)

# Enviar el mensaje a los destinatarios
smtp_server.sendmail(smtp_username, to_addresses, msg.as_string())

# Cerrar la conexión con el servidor SMTP
smtp_server.quit()
