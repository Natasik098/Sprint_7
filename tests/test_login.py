import allure
import pytest
import requests

from urls import Urls
from handle import Handle
from data import Users, Messages

class TestCourierLogin:

    @allure.title("Успешная авторизация курьера") 
    def test_login_courier_success(self, registered_courier): 
        response = requests.post( 
            f"{Urls.URL}{Handle.LOGIN_COURIER}", 
            json={ 
                "login": registered_courier["login"], 
                "password": registered_courier["password"] 
            } 
        )
        response_json = response.json() 

        assert response.status_code == 200 
        assert "id" in response.json()
        assert isinstance(response_json["id"], int)

    @allure.title("Ошибка при авторизации с невалидными данными") 
    def test_login_wrong_password(self, registered_courier): 
        response = requests.post( 
            f"{Urls.URL}{Handle.LOGIN_COURIER}", 
            json={
                "login": registered_courier["login"], 
                "password": Users.WRONG_PASSWORD 
            } 
        ) 

        response_json = response.json()

        assert response.status_code == 404
        assert response_json["message"] == Messages.LOGIN_NOT_FOUND 
        
    @allure.title("Ошибка при отсутствии обязательного поля логин") 
    def test_login_without_login(self, registered_courier): 
            login_data = {
                 "password": registered_courier["password"]
            }

            response = requests.post( 
                f"{Urls.URL}{Handle.LOGIN_COURIER}", 
                json=login_data
            )

            response_json = response.json()

            assert response.status_code == 400
            assert response_json["message"] == Messages.LOGIN_DATA_REQUIRED