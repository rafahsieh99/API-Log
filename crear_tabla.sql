CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    log_level VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    received_at TIMESTAMP NOT NULL
);
