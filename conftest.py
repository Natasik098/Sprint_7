import pytest 
import requests

from generator import register_new_courier
from urls import Urls
from handle import Handle

#Возвращает новые данные курьера
@pytest.fixture
def courier_data():
    return register_new_courier()

#Создает курьера и возвращает его данные
@pytest.fixture
def registered_courier():
    courier = register_new_courier()

    response = requests.post(
        f"{Urls.URL}{Handle.CREATE_COURIER}",
        json=courier
    )

    assert response.status_code == 201, (
        f"Курьер не создан: {response.status_code}, {response.text}"
    )
    assert response.json() == {"ok": True}
    return courier