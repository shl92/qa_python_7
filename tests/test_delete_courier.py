import requests
import allure
from data import URLS, Profile, StatusCode, TextMessage
from api.profile_api_methods import ProfileMethods
from api.check_api_methods import CheckMethods


@allure.feature("Проверка ручки удаления курьера")
class TestDeleteCourier:
    @allure.title("Проверка успешного удаления курьера")
    @allure.step("Создаем курьера и логинимся в систему, отправляем запрос на удаление курьера, проверяем код ответа, "
                 "проверяем текст ответа")
    def test_delete_courier_success(self):
        _, profile_data = ProfileMethods.create_courier()
        profile_id = ProfileMethods.login_courier(profile_data)
        response = requests.delete(f"{URLS.ENDPOINT_CREATE_OR_DELETE_COURIER}/{profile_id}")
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_text_message(response, TextMessage.TRUE_MESSAGE)

    @allure.title("Проверка получения ошибки при попытке удалить курьера с некорректным ID курьера")
    @allure.step("Отправляем запрос на удаление курьера с передачей некорректного ID курьера, проверяем код ответа, "
                 "проверяем текст ответа")
    def test_delete_courier_wrong_id(self):
        response = requests.delete(f"{URLS.ENDPOINT_CREATE_OR_DELETE_COURIER}/{Profile.WRONG_ID}")
        CheckMethods.check_status_code(response, StatusCode.CODE_404)
        CheckMethods.check_json_message(response, TextMessage.NO_COURIER_ID)

    @allure.title("Проверка получения ошибки при попытке удалить курьера без передачи ID курьера")
    @allure.step("Отправляем запрос на удаление курьера без передачи ID курьера, проверяем код ответа, проверяем "
                 "текст ответа")
    def test_delete_courier_no_id(self):
        response = requests.delete(URLS.ENDPOINT_CREATE_OR_DELETE_COURIER)
        CheckMethods.check_status_code(response, StatusCode.CODE_404)
        CheckMethods.check_json_message(response, TextMessage.NOT_FOUND)
