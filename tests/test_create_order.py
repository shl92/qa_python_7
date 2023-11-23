import requests
import pytest
import allure
import json
from data import URLS, Order, StatusCode, TextMessage
from api.check_api_methods import CheckMethods


@allure.feature("Проверка ручки создания заказа")
class TestCreateOrder:
    @allure.title("Проверка успешного создания заказа с разными цветами самоката")
    @allure.description("Устанавливаем тестируемый цвет, отправляем запрос на создание заказа, проверяем код ответа, "
                        "проверяем текста ответа на наличие track номера")
    @pytest.mark.parametrize('color', [Order.BLACK_COLOR, Order.GREY_COLOR, Order.BOTH_COLOR, Order.EMPTY_DATA],
                             ids=['black_color', 'grey_color', 'black_and_grey_colors', 'no_color'])
    def test_create_order_different_colors(self, cansel_order, color):
        payload = Order.order_data
        payload['color'] = color
        response = requests.post(URLS.ENDPOINT_CREATE_OR_GET_ORDER, data=json.dumps(payload))
        CheckMethods.check_status_code(response, StatusCode.CODE_201)
        CheckMethods.check_text_in_json(response, TextMessage.TRACK)
        cansel_order.append(response.json()['track'])
