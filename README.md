
[![Apache 2.0 License](https://img.shields.io/badge/License-Apache-green.svg)](https://choosealicense.com/licenses/apache/)
![Docker Image Version](https://img.shields.io/docker/v/sxmxc/ssl_checker_api)
![GitHub Sponsors](https://img.shields.io/github/sponsors/sxmxc)


**Built using:**
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-009485.svg?logo=fastapi&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](#)


# SSL Checker API

SSL Checker API is a simple FastAPI-based service that provides SSL certificate validation for any given host. It acts as a RESTful wrapper around the [ssl-checker](https://github.com/narbehaj/ssl-checker) Python script, making it easy to integrate SSL certificate checks into your applications.


## Features  

- **Health Check Endpoint (`/ping`)**: Quick status check to ensure the API is running.  
- **SSL Check Endpoint (`/check/{host}`)**: Fetches SSL certificate details for a given host, including validity, expiration, and issuer details.  
- **Fast & Lightweight**: Built using FastAPI for high performance and easy scalability.  
- **JSON Response**: Structured output for seamless integration with other applications.  


## Endpoints  

### Health Check  

**GET `/ping`**  
Returns a basic health check response to confirm the API is operational.  

#### Response:
```json
{
  "dang_ol": "pong",
  "server_timestamp": "2025-02-08T12:00:00.000000",
  "status": "ok"
}
```

### SSL Certificate Check

**GET `/check/{host}`**
Fetches SSL certificate details for the given host.
**Parameters:**
- `host` (string, required): The domain name of the URL to check

#### Response:
```json
{
  "api-version": "1.0",
  "app": "ssl-checker-api",
  "host": "example.com",
  "status": "ok",
  "result": {
    "issuer": "Let's Encrypt",
    "valid_from": "2025-01-01",
    "valid_to": "2025-04-01",
    "days_remaining": 52,
    "status": "valid"
  }
}
```
## Installation

**1. Clone the repository**
```bash
  git clone https://github.com/sxmxc/ssl-checker-api.git  
  cd ssl-checker-api  

```

**2. Install dependencies**
```bash
  pip install -r requirements.txt
```

**3. Run the API**
```bash
  python app/main.py 
```

**4. Access API documentation**
- Open http://localhost:8000/docs for interactive Swagger UI.
- Open http://localhost:8000/redoc for ReDoc API documentation.
    
## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)

