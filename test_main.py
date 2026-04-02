from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_current_time():
    """Test that /time endpoint returns correct format and status code"""
    response = client.get("/time")

    # Check status code
    assert response.status_code == 200

    # Check response structure
    data = response.json()
    assert "Año-Mes-Día" in data
    assert "Hora:Minutos:Segundo" in data

    # Check format of Año-Mes-Día (should be YYYY-M-D)
    fecha = data["Año-Mes-Día"]
    assert isinstance(fecha, str)
    partes_fecha = fecha.split("-")
    assert len(partes_fecha) == 3

    # Check format of Hora:Minutos:Segundo (should be H:M:S)
    hora = data["Hora:Minutos:Segundo"]
    assert isinstance(hora, str)
    partes_hora = hora.split(":")
    assert len(partes_hora) == 3


def test_time_endpoint_returns_json():
    """Test that /time endpoint returns valid JSON"""
    response = client.get("/time")
    assert response.headers["content-type"] == "application/json"


def test_time_values_are_valid_integers():
    """Test that time values are valid integers"""
    response = client.get("/time")
    data = response.json()

    # Parse and validate fecha components
    year, month, day = map(int, data["Año-Mes-Día"].split("-"))
    assert 2000 <= year <= 2100
    assert 1 <= month <= 12
    assert 1 <= day <= 31

    # Parse and validate hora components
    hour, minute, second = map(int, data["Hora:Minutos:Segundo"].split(":"))
    assert 0 <= hour <= 23
    assert 0 <= minute <= 59
    assert 0 <= second <= 59
