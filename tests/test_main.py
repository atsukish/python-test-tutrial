"""main.pyのテスト"""
from http import HTTPStatus

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health() -> None:

    response = client.get("/health")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"health": "OK"}


def test_price() -> None:

    item1 = {
        "name": "ice cream",
        "price": 100,
        "is_reduce_tax": True,
    }
    response = client.post("/tax_price", json=item1)
    assert response.status_code == HTTPStatus.OK
    assert response.json()["price_with_tax"] == 108

    item2 = {
        "name": "beer",
        "price": 180,
        "is_reduce_tax": False,
    }
    response = client.post("/tax_price", json=item2)
    assert response.status_code == HTTPStatus.OK
    assert response.json()["price_with_tax"] == 198
