import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hola_mundo(client):

    # Simulamos una visita a la página principal
    response = client.get('/')
    
    # Verificamos que cargue bien (200 OK) y que contenga el texto
    assert response.status_code == 200
    assert b"Hola Mundo" in response.data