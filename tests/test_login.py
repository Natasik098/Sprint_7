import allure
import requests

from urls import Urls
from handle import Handle
from data import Users

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
        assert response.status_code == 200 
        assert "id" in response.json() 

    @allure.title("Ошибка при авторизации с невалидными данными") 
    def test_login_with_invalid_data(self, registered_courier): 
        response = requests.post( 
            f"{Urls.URL}{Handle.LOGIN_COURIER}", 
            json={
                "login": registered_courier["login"], 
                "password": Users.WRONG_PASSWORD 
            } 
        ) 
        assert response.status_code == 404 
        
    @allure.title("Ошибка при отсутствии обязательного поля логин") 
    def test_login_without_login(self, registered_courier): 
            response = requests.post( 
                f"{Urls.URL}{Handle.LOGIN_COURIER}", 
                json={ "password": registered_courier["password"] 
                } 
            )
            assert response.status_code == 400