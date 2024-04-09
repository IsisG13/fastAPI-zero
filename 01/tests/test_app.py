from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app) # Arrange (organizar)

    response = client.get('/') # Act (agir)

    assert response.status_code == 200 # Assert (afirmar)
    assert response.json() == {'message': 'Olá Mundo!'} # Assert (afirmar)
