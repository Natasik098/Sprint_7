#Итоговый проект 7 — тестирование API Яндекс Самоката

##Описание проекта

Проект предназначен для автоматизированного тестирования API учебного сервиса Яндекс Самокат.

##Используемые технологии

Python

pytest

requests

Faker

Allure Pytest

###Структура проекта

tests/test_courier.py — тесты создания курьера.

tests/test_login.py — тесты авторизации курьера.

tests/test_order.py — тесты создания заказа.

tests/test_orders_list.py — тест получения списка заказов.

conftest.py — фикстуры pytest.

generator.py — генерация тестовых данных с F


aker.

data.py — постоянные тестовые данные.

urls.py — базовый URL сервиса.

handle.py — эндпоинты API.

Установка зависимостей

python -m pip install -r requirements.txt

Запуск всех тестов

pytest -v

Запуск тестов с результатами для Allure

pytest --alluredir=allure-results

Формирование отчёта Allure

allure serve allure-results