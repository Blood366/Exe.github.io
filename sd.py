from twilio.rest import Client
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Configura tus credenciales de Twilio desde variables de entorno
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

# Inicializa el cliente de Twilio
client = Client(account_sid, auth_token)

def enviar_mensaje_whatsapp(mensaje, numero_destino):
    """
    Envía un mensaje de WhatsApp a través de la API de Twilio.

    Parámetros:
    mensaje (str): El contenido del mensaje a enviar.
    numero_destino (str): El número de destino en formato internacional (incluye el código de país).
    """
    try:
        mensaje_enviado = client.messages.create(
            from_='whatsapp:+14155238886',  # Número de WhatsApp de Twilio
            body=mensaje,
            to=f'whatsapp:{numero_destino}' if 'whatsapp:' not in numero_destino else numero_destino
        )
        print(f"Mensaje enviado con éxito. SID: {mensaje_enviado.sid}")
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    mensaje = "Hola, este es un mensaje de prueba desde Python."
    numero_destino = "+18299841391"  # Reemplaza con el número de destino en formato internacional
    enviar_mensaje_whatsapp(mensaje, numero_destino)
