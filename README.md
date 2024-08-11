# API-Log
Este proyecto implementa un sistema de logging distribuido en el que varios servicios generan y envían logs a un servidor central. El servidor central recibe estos logs y los almacena en una base de datos PostgreSQL para su posterior análisis.

## Descripción General

El sistema consiste en dos servicios simulados que generan logs con datos aleatorios y un servidor central que recibe, autentica y almacena estos logs en la base de datos. Los logs contienen información como la fecha y hora de generación, el nombre del servicio, el nivel de severidad, y un mensaje descriptivo.

## Tecnologías Utilizadas

- **Python 3**
- **Flask** para el servidor central.
- **PostgreSQL** para la base de datos.
- **psycopg2** para la conexión con PostgreSQL.
- **requests** para que los servicios simulados envíen los logs al servidor.

## Configurar PostgreSQL
### Crear base de datos en PostgreSql
CREATE DATABASE nombre_base_datos;

### Crear la tabla logs en la base de datos:
CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    service_name VARCHAR(50),
    log_level VARCHAR(10),
    message TEXT,
    received_at TIMESTAMP
);

## Configurar el servidor:
Abre el archivo server.py y configura los detalles de la base de datos:
db_config = {
    "dbname": "nombre_base_datos",
    "user": "usuario",
    "password": "contraseña",
    "host": "localhost"
}

## Consultar la Base de Datos
SELECT * FROM logs;

