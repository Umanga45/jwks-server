from flask import Flask, jsonify, request
from jwks import JWKS
from auth import issue_jwt

app = Flask(__name__)

# Initialize JWKS (Key Storage) and generate an initial RSA key
jwks = JWKS()
jwks.generate_rsa_key()

# RESTful endpoint to return the public JWKS
@app.route('/.well-known/jwks.json', methods=['GET'])
def get_jwks():
    keys = jwks.get_public_keys()
    return jsonify({"keys": keys})

# Authentication endpoint that issues JWTs (Handles expired query parameter)
@app.route('/auth', methods=['POST'])
def auth():
    expired = request.args.get('expired')
    token = issue_jwt(jwks, expired=bool(expired))
    return jsonify({"token": token})

if __name__ == '__main__':
    app.run(port=8080)
