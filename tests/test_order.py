import allure
import pytest
import requests

from urls import Urls
from handle import Handle
from generator import generate_order_data
from data import Orders

class TestCreateOrder:

    @pytest.mark.parametrize(
        "color",
        Orders.COLORS,
        ids=[
            "без цвета",
            "черный самокат",
            "серый самокат",
            "два цвета"
        ]
    )
    @allure.title("Можно создать заказ с разными вариантами цвета")
    def test_create_order_with_different_colors(self, color):
        order_data = generate_order_data()
        order_data["color"] = color

        response = requests.post(
            f"{Urls.URL}{Handle.CREATE_ORDER}",
            json=order_data
        )

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)