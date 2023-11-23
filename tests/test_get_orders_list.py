import requests
import allure
from data import URLS, Profile, StatusCode, TextMessage
from api.check_api_methods import CheckMethods


@allure.feature("Проверка ручки получения списка заказов")
class TestGetOrdersList:
    @allure.title("Проверка успешного получения списка заказов по ID курьера")
    @allure.description("Отправляем запрос на получение списка заказов, проверяем код ответа, проверяем текст ответа "
                        "на наличие списка заказов по ключу 'orders' в ответе ")
    def test_get_orders_list_success(self):
        payload = {"courierId": Profile.ID}
        response = requests.get(URLS.ENDPOINT_CREATE_OR_GET_ORDER, params=payload)
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_orders_list(response)

    @allure.title("Проверка получения ошибки при получении списка заказа с некорректным ID курьера")
    @allure.description("Отправляем запрос на получение списка заказов с передачей некорректного ID курьера, "
                        "проверяем код ответа, проверяем текст ответа")
    def test_get_orders_list_wrong_id(self):
        payload = {"courierId": Profile.WRONG_ID}
        response = requests.get(URLS.ENDPOINT_CREATE_OR_GET_ORDER, params=payload)
        CheckMethods.check_status_code(response, StatusCode.CODE_404)
        CheckMethods.check_json_message(response, TextMessage.NO_COURIER_IDENT)
