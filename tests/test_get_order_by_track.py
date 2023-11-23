import requests
import allure
from data import URLS, Order, StatusCode, TextMessage
from api.order_api_methods import OrderMethods
from api.check_api_methods import CheckMethods


@allure.feature("Проверка ручки получения заказа")
class TestGetOrder:
    @allure.title("Проверка успешного получения заказа по track номеру")
    @allure.description("Создаем заказ и получаем track номер, отправляем запрос на получение заказа по track номеру, "
                        "проверяем код ответа, проверяем наличие ключа 'order' в тексте ответа")
    def test_get_order_by_track_success(self, cansel_order):
        track_id = OrderMethods.create_order_and_get_track()
        params = {"t": track_id}
        response = requests.get(URLS.ENDPOINT_GET_ORDER_BY_TRACK, params=params)
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_text_in_json(response, TextMessage.ORDER)
        cansel_order.append(track_id)

    @allure.title("Проверка получения ошибки при получении заказа с некорректным track номером")
    @allure.description("Отправляем запрос на получение заказа с передачей некорректного track номера, проверяем код "
                        "ответа, проверяем текст ответа")
    def test_get_order_by_track_wrong_track(self):
        params = {"t": Order.WRONG_TRACK}
        response = requests.get(URLS.ENDPOINT_GET_ORDER_BY_TRACK, params=params)
        CheckMethods.check_status_code(response, StatusCode.CODE_404)
        CheckMethods.check_json_message(response, TextMessage.TRACK_NOT_FOUND)

    @allure.title("Проверка получения ошибки при получении заказа без передачи track номера")
    @allure.description("Отправляем запрос на получение заказа без передачи track номера, проверяем код ответа, "
                        "проверяем текст ответа")
    def test_get_order_by_track_no_track(self):
        params = {"t": Order.EMPTY_DATA}
        response = requests.get(URLS.ENDPOINT_GET_ORDER_BY_TRACK, params=params)
        CheckMethods.check_status_code(response, StatusCode.CODE_400)
        CheckMethods.check_json_message(response, TextMessage.NOT_ENOUGH_DATA_FOR_SEARCH)
