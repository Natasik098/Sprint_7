import allure
import requests

from urls import Urls
from handle import Handle

class TestOrdersList:

    @allure.title("Можно получить список заказов")
    def test_get_orders_list(self):
        response = requests.get(
            f"{Urls.URL}{Handle.ORDERS_LIST}"
        )

        assert response.status_code == 200

        response_body = response.json()

        assert isinstance(response_body, dict)
        assert "orders" in response_body
        assert isinstance(response_body["orders"], list)