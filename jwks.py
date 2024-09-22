import time
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class JWKS:
    def __init__(self):
        self.keys = []  # List to store generated keys

    def generate_rsa_key(self):
        # Generate a new RSA private key
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        
        # Generate a unique key ID (kid)
        kid = str(len(self.keys) + 1)
        
        # Key expiration time (1 hour from now)
        expiry = int(time.time()) + 3600

        # Store keys in PEM format
        public_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                             format=serialization.PublicFormat.SubjectPublicKeyInfo)
        private_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PrivateFormat.PKCS8,
                                                encryption_algorithm=serialization.NoEncryption())
        
        # Save key data with expiry and kid
        self.keys.append({
            "kid": kid,
            "private_key": private_pem,
            "public_key": public_pem.decode('utf-8'),
            "expiry": expiry
        })

    # Return public keys that haven't expired
    def get_public_keys(self):
        return [
            {
                "kid": key["kid"],
                "kty": "RSA",
                "use": "sig",
                "alg": "RS256",
                "n": key["public_key"],
                "e": "AQAB"
            }
            for key in self.keys if key["expiry"] > time.time()
        ]
