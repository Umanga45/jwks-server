import pytest
from app import app

def test_jwks():
    client = app.test_client()
    response = client.get('/.well-known/jwks.json')
    assert response.status_code == 200
    assert "keys" in response.json

def test_jwt():
    client = app.test_client()
    response = client.post('/auth')
    assert response.status_code == 200
    assert "token" in response.json
