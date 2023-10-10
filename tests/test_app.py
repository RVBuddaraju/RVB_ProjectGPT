import pytest
from app import app  # Import your app as created in app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_root(client):
    response = client.get('/')
    assert response.status_code == 200
