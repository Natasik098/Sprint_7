import allure
import pytest
import requests

from urls import Urls
from handle import Handle
from data import Messages
from generator import (
    register_new_courier,
    register_new_courier_without_login,
    register_new_courier_without_password
)

class TestCourier:

    @allure.title("Курьера можно создать с корректными данными")
    def test_create_courier(self):
        courier = register_new_courier()

        response = requests.post(
            f"{Urls.URL}{Handle.CREATE_COURIER}",
            json=courier
        )

        response_json = response.json()

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух курьеров с одинаковым логином")
    def test_create_duplicate_courier(self):
        courier = register_new_courier()

        first_response = requests.post(
            f"{Urls.URL}{Handle.CREATE_COURIER}",
            json=courier
        )
        second_response = requests.post(
            f"{Urls.URL}{Handle.CREATE_COURIER}",
            json=courier
        )

        response_json = second_response.json()
        assert first_response.status_code == 201
        assert second_response.status_code == 409
        assert response_json["message"] ==Messages.COURIER_ALREADY_EXISTS

    @pytest.mark.parametrize(
        "courier_data",
        [
            register_new_courier_without_login()
        ],
        ids=["без логина"]
    )

    @allure.title("Нельзя создать курьера без обязательного поля")
    def test_create_courier_without_required_field(self, courier_data):
        response = requests.post(
            f"{Urls.URL}{Handle.CREATE_COURIER}",
            json=courier_data
        )

        response_json = response.json()
    
        assert response.status_code == 400
        assert response_json["message"] == Messages.COURIER_DATA_REQUIRED