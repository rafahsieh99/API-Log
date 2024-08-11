import requests
import json
import time
import random
from datetime import datetime

# Configuración del servicio
SERVICE_NAME = "Servicio2"
LOGGING_SERVER_URL = "http://localhost:5000/logs"
API_TOKEN = "service-2-token"

def generate_log():
    log_levels = ["INFO", "ERROR", "DEBUG", "WARNING"]
    log = {
        "timestamp": datetime.now().isoformat(),
        "service_name": SERVICE_NAME,
        "log_level": random.choice(log_levels),
        "message": f"Prueba de mensaje {SERVICE_NAME}"
    }
    return log

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

if __name__ == "__main__":
    while True:
        log = generate_log()
        send_log(log)
        time.sleep(random.randint(1, 5))
