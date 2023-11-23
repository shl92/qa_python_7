import pytest
import allure
import requests
from data import URLS, StatusCode
from api.check_api_methods import CheckMethods


@allure.step("Отправляем запрос на отмену заказа и проверяем код ответа")
@pytest.fixture
def cansel_order():
    track = list()
    yield track
    response_cansel = requests.put(f"{URLS.ENDPOINT_CANSEL_ORDER}?track={track[0]}")
    CheckMethods.check_status_code(response_cansel, StatusCode.CODE_200)


@allure.step("Отправляем запрос на завершение заказа, находящегося в работе, и проверяем код ответа")
@pytest.fixture
def cansel_order_in_work():
    track = list()
    yield track
    response_cansel = requests.put(f"{URLS.ENDPOINT_FINISH_ORDER}{track[0]}")
    CheckMethods.check_status_code(response_cansel, StatusCode.CODE_200)


@allure.step("Отправляем запрос на удаление курьера и проверяем код ответа")
@pytest.fixture
def delete_courier():
    id = list()
    yield id
    response = requests.delete(f"{URLS.ENDPOINT_CREATE_OR_DELETE_COURIER}/{id[0]}")
    CheckMethods.check_status_code(response, StatusCode.CODE_200)
