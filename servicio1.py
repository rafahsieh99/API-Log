import requests
import json
import time
import random
from datetime import datetime

# Configuración del servicio
SERVICE_NAME = "Servicio1"
LOGGING_SERVER_URL = "http://localhost:5000/logs"  # URL del servidor central
API_TOKEN = "service-1-token"  # Token de autenticación

# Función para generar logs simulados
def generate_log():
    log_levels = ["INFO", "ERROR", "DEBUG", "WARNING"]
    log = {
        "timestamp": datetime.now().isoformat(),
        "service_name": SERVICE_NAME,
        "log_level": random.choice(log_levels),
        "message": f"Prueba de mensaje {SERVICE_NAME}"
    }
    return log

# Función para enviar logs al servidor central
def send_log(log):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(LOGGING_SERVER_URL, headers=headers, data=json.dumps(log))
    if response.status_code == 200:
        print("Log enviado correctamente")
    else:
        print(f"Error al enviar log: {response.status_code} - {response.text}")

# Bucle principal
if __name__ == "__main__":
    while True:
        log = generate_log()
        send_log(log)
        time.sleep(random.randint(1, 5))  # Esperar entre 1 y 5 segundos antes de enviar el próximo log
