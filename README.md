# JWKS Server Project

This is a simple JWKS (JSON Web Key Set) server that serves public keys for verifying JSON Web Tokens (JWTs). The server can generate RSA key pairs, associate unique `kid` (key IDs) with them, and handle key expiry.

## Features
- RSA key pair generation with unique `kid` and expiry timestamp.
- RESTful JWKS endpoint to serve public keys that haven't expired.
- `/auth` endpoint to issue JWTs.
- Supports the `expired=true` query parameter to issue JWTs with expired keys.

## Requirements
- Python 3.11 or higher
- Dependencies listed in `requirements.txt`

## Setup Instructions

### 1. Clone the Repository
To get started, clone the repository to your local machine:

git clone https://github.com/Umanga45/jwks-server.git
cd jwks-server
Install Dependencies
Install the required Python packages by running:
pip install -r requirements.txt
3. Run the Server
Start the JWKS server by running: 
python app.py
The server will run on http://127.0.0.1:8080.

4. Test the JWKS Endpoint
To check the public keys, visit:
http://127.0.0.1:8080/.well-known/jwks.json
5. Test the /auth Endpoint
To get a JWT, run:
curl -X POST http://127.0.0.1:8080/auth
To get an expired JWT, run:
curl -X POST http://127.0.0.1:8080/auth?expired=true
6. Run Tests
To ensure everything works, run the tests:
python -m pytest --cov=app tests/
