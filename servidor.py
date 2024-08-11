from flask import Flask, request, jsonify
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Configuración de la conexión a la base de datos
conn = psycopg2.connect(
    dbname="API",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Tokens de autenticación válidos
# Tokens de autenticación válidos
VALID_TOKENS = {
    "service-1-token": "Servicio1",
    "service-2-token": "Servicio2",  # Agrega más tokens según sea necesario
}


# Endpoint para recibir los logs
@app.route('/logs', methods=['POST'])
def receive_log():
    auth_header = request.headers.get('Authorization')
    
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Token no proporcionado"}), 401

    token = auth_header.split(" ")[1]

    if token not in VALID_TOKENS:
        return jsonify({"error": "Token no válido"}), 403

    # Procesar el log
    log = request.json
    received_at = datetime.now().isoformat()
    query = """
        INSERT INTO logs (timestamp, service_name, log_level, message, received_at)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        log['timestamp'], 
        log['service_name'], 
        log['log_level'], 
        log['message'], 
        received_at
    ))
    conn.commit()

    return jsonify({"message": "Log recibido y almacenado"}), 200

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)

