import requests
import pytest
import allure
from data import URLS, Profile, StatusCode, TextMessage
from api.check_api_methods import CheckMethods


@allure.feature("Проверка ручки логина курьера в системе")
class TestLogin:
    @allure.title("Проверка успешного логина в систему")
    @allure.description("Отправка запроса на логин в систему, проверка кода ответа, проверка соответствия ID курьера, "
                        "полученного в тексте ответа, с переданным ID курьера в запросе")
    def test_login_courier_success(self):
        payload = {"login": Profile.LOGIN,
                   "password": Profile.PASSWORD}
        response = requests.post(URLS.ENDPOINT_LOGIN, data=payload)
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_json_id(response)

    @allure.title("Проверка получения ошибки при логине без логина/пароля")
    @allure.description("Отправка запроса на логин в систему без пароля/логина, проверка кода ответа, проверка текста "
                        "ответа")
    @pytest.mark.parametrize('login, password', [(Profile.LOGIN, ''), ('', Profile.PASSWORD)],
                             ids=['without_login', 'without_password'])
    def test_login_courier_error_not_all_data(self, login, password):
        payload = {"login": login,
                   "password": password}
        response = requests.post(URLS.ENDPOINT_LOGIN, data=payload)
        CheckMethods.check_status_code(response, StatusCode.CODE_400)
        CheckMethods.check_json_message(response, TextMessage.NOT_ENOUGH_DATA_FOR_LOGIN)

    @allure.title("Проверка получения ошибки при логине с некорректным логином/паролем")
    @allure.description("Отправка запроса на логин в систему с некорректными логином/паролем, проверка кода ответа, "
                        "проверка текста ответа")
    @pytest.mark.parametrize('login, password', [(Profile.LOGIN, Profile.PASSWORD_WRONG),
                                                 (Profile.LOGIN_WRONG, Profile.PASSWORD)],
                             ids=['wrong_password', 'wrong_login'])
    def test_login_courier_wrong_data(self, login, password):
        payload = {"login": login,
                   "password": password}
        response = requests.post(URLS.ENDPOINT_LOGIN, data=payload)
        CheckMethods.check_status_code(response, StatusCode.CODE_404)
        CheckMethods.check_json_message(response, TextMessage.NO_PROFILE)
