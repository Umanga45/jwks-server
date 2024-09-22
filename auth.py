import jwt
import time

def issue_jwt(jwks, expired=False):
    # Use the first key from the JWKS store
    key_data = jwks.keys[0]
    kid = key_data['kid']
    private_key = key_data['private_key']
    
    # Determine the expiration time (expired or valid)
    expiry_time = int(time.time()) - 3600 if expired else int(time.time()) + 3600
    
    # JWT payload (claims)
    payload = {
        "sub": "fakeuser",
        "iat": int(time.time()),
        "exp": expiry_time
    }
    
    # Create the JWT with the RS256 algorithm and kid in the header
    token = jwt.encode(payload, private_key, algorithm='RS256', headers={'kid': kid})
    return token
