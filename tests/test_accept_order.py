import requests
import allure
from data import URLS, StatusCode, TextMessage, Order, Profile
from api.profile_api_methods import ProfileMethods
from api.order_api_methods import OrderMethods
from api.check_api_methods import CheckMethods


@allure.feature("Проверка ручки принятия заказа")
class TestAcceptOrder:
    @allure.title("Проверка успешного принятия заказа")
    @allure.description("Создаем профиль курьера и логинимся в систему, создаем заказ и получаем track номер, "
                        "получаем ID заказа по track номеру, отправляем запрос на принятие заказа, проверяем код "
                        "ответа, проверяем текст ответа")
    def test_accept_order_success(self, cansel_order_in_work, delete_courier):
        _, profile_data = ProfileMethods.create_courier()
        courier_id = ProfileMethods.login_courier(profile_data)
        track_id = OrderMethods.create_order_and_get_track()
        id_order = OrderMethods.get_order_id_by_track(track_id)
        payload = {"id": id_order,
                   "courierId": courier_id}
        response = requests.put(f"{URLS.ENDPOINT_ACCEPT_ORDER}{payload['id']}?courierId={payload['courierId']}")
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_text_message(response, TextMessage.TRUE_MESSAGE)
        cansel_order_in_work.append(id_order)
        delete_courier.append(courier_id)

    @allure.title("Проверка получения ошибки при принятии заказа без передачи ID курьера")
    @allure.description("Создаем заказ и получаем track номер, получаем ID заказа по track номеру, отправляем запрос "
                        "на принятие заказа без передачи ID курьера, проверяем код ответа, проверяем текст ответа")
    def test_no_courier_id(self, cansel_order):
        track_id = OrderMethods.create_order_and_get_track()
        id_order = OrderMethods.get_order_id_by_track(track_id)
        payload = {"id": id_order}
        response = requests.put(f"{URLS.ENDPOINT_ACCEPT_ORDER}{payload['id']}")
        CheckMethods.check_status_code(response, StatusCode.CODE_400)
        CheckMethods.check_json_message(response, TextMessage.NOT_ENOUGH_DATA_FOR_SEARCH)
        cansel_order.append(track_id)

    @allure.title("Проверка получения ошибки при принятии заказа без передачи ID заказа")
    @allure.description("Создаем профиль курьера и логинимся в систему, отправляем запрос на принятие заказа без "
                        "передачи ID заказа, проверяем код ответа, проверяем текст ответа")
    def test_no_order_id(self, delete_courier):
        _, profile_data = ProfileMethods.create_courier()
        courier_id = ProfileMethods.login_courier(profile_data)
        payload = {"courierId": courier_id}
        response = requests.put(f"{URLS.ENDPOINT_ACCEPT_ORDER}courierId={payload['courierId']}")
        CheckMethods.check_status_code(response, StatusCode.CODE_400)
        CheckMethods.check_json_message(response, TextMessage.NOT_ENOUGH_DATA_FOR_SEARCH)
        delete_courier.append(courier_id)

    @allure.title("Проверка получения ошибки при принятии заказа с передачей некорректного ID курьера")
    @allure.description("Создаем заказ и получаем track номер, получаем ID заказа по track номеру, отправляем запрос "
                        "на принятие заказа с передачей некорректного ID курьера, проверяем код ответа, проверяем "
                        "текст ответа")
    def test_wrong_courier_id(self, cansel_order):
        track_id = OrderMethods.create_order_and_get_track()
        id_order = OrderMethods.get_order_id_by_track(track_id)
        payload = {"id": id_order,
                   "courierId": Profile.WRONG_ID}
        response = requests.put(f"{URLS.ENDPOINT_ACCEPT_ORDER}{payload['id']}?courierId={payload['courierId']}")
        CheckMethods.check_status_code(response, StatusCode.CODE_404)
        CheckMethods.check_json_message(response, TextMessage.NO_COURIER_ID_EXIST)
        cansel_order.append(track_id)

    @allure.title("Проверка получения ошибки при принятии заказа с передачей некорректного ID заказа")
    @allure.description("Создаем профиль курьера и логинимся в систему, отправляем запрос на принятие заказа с "
                        "передачей некорректного ID заказа, проверяем код ответа, проверяем текст ответа")
    def test_wrong_order_id(self, delete_courier):
        _, profile_data = ProfileMethods.create_courier()
        courier_id = ProfileMethods.login_courier(profile_data)
        payload = {"id": Order.ORDER_WRONG_ID,
                   "courierId": courier_id}
        response = requests.put(f"{URLS.ENDPOINT_ACCEPT_ORDER}{payload['id']}?courierId={payload['courierId']}")
        CheckMethods.check_status_code(response, StatusCode.CODE_404)
        CheckMethods.check_json_message(response, TextMessage.NO_ORDER_ID)
        delete_courier.append(courier_id)
