# Cloud Monitoring API

A Flask-based REST API for cloud monitoring and health checks.
Dockerized and documented using Swagger.

## Features
- Flask REST API
- Swagger UI
- Health Check Endpoint
- Dockerized
- Unit Testing

## Endpoint
GET /health/

## Run with Docker

docker build -t flask-monitor .
docker run -d -p 5000:5000 flask-monitor

## Swagger UI
http://<EC2_PUBLIC_IP>:5000/

## Testing
docker exec -it flask-app python3 test_app.py

## Author
Divyansh Sharma

