import allure
import pytest
import requests

from urls import Urls
from handle import Handle
from generator import (
    register_new_courier_without_login,
    register_new_courier_without_password
)

class TestCreateCourier:

    @allure.title("Курьера можно создать с корректными данными")
    def test_create_courier_success(self, courier_data):
        response = requests.post(
            f"{Urls.URL}{Handle.CREATE_COURIER}",
            json=courier_data
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух курьеров с одинаковым логином")
    def test_create_duplicate_courier(self, registered_courier):
        response = requests.post(
            f"{Urls.URL}{Handle.CREATE_COURIER}",
            json=registered_courier
        )

        assert response.status_code == 409
        assert "Этот логин уже используется. Попробуйте другой." in response.text

    @pytest.mark.parametrize(
        "courier_without_field",
        [
            register_new_courier_without_login,
            register_new_courier_without_password
        ],
        ids=["без логина", "без пароля"]
    )
    @allure.title("Нельзя создать курьера без обязательного поля")
    def test_create_courier_without_required_field(
        self, courier_without_field
    ):
        courier = courier_without_field()

        response = requests.post(
            f"{Urls.URL}{Handle.CREATE_COURIER}",
            json=courier
        )

        assert response.status_code == 400
        assert (
            "Недостаточно данных для создания учетной записи"
            in response.text
        )