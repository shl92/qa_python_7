import allure
import requests
import pytest
from data import URLS, Profile, StatusCode, TextMessage
from api.profile_api_methods import ProfileMethods
from api.check_api_methods import CheckMethods


@allure.feature("Проверка ручки создания курьера")
class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    @allure.description("Создаем данные для профиля курьера, отправляем запрос на создание курьера, проверяем код "
                        "ответа, проверяем текст ответа")
    def test_create_courier_success_new_courier(self, delete_courier):
        response, profile = ProfileMethods.create_courier()
        CheckMethods.check_status_code(response, StatusCode.CODE_201)
        CheckMethods.check_text_message(response, TextMessage.TRUE_MESSAGE)
        delete_courier.append(ProfileMethods.login_courier(profile))

    @allure.title("Проверка получения ошибки при повторном создании курьера с уже существующим профилем")
    @allure.description("Отправляем запрос на создание курьера с данными уже существующего профиля, проверяем код "
                        "ответа, проверяем текст ответа")
    def test_create_courier_the_same_courier_error(self):
        payload = {"login": Profile.LOGIN,
                   "password": Profile.PASSWORD}
        response = requests.post(URLS.ENDPOINT_CREATE_OR_DELETE_COURIER, data=payload)
        CheckMethods.check_status_code(response, StatusCode.CODE_409)
        CheckMethods.check_json_message(response, TextMessage.LOGIN_ALREADY_USE)

    @allure.title("Проверка получения ошибки при создании курьера без логина/пароля")
    @allure.description("Создаем данные для профиля курьера, отправляем запрос на создание курьера без логина/пароля, "
                        "проверяем код ответа, проверяем текст ответа")
    @pytest.mark.parametrize('login, password', [(ProfileMethods.courier_generate_profile()['login'], ''),
                                                 ('', ProfileMethods.courier_generate_profile()['password'])],
                             ids=['without_login', 'without_password'])
    def test_create_courier_error_not_all_data(self, login, password):
        payload = {"login": login,
                   "password": password}
        response = requests.post(URLS.ENDPOINT_CREATE_OR_DELETE_COURIER, data=payload)
        CheckMethods.check_status_code(response, StatusCode.CODE_400)
        CheckMethods.check_json_message(response, TextMessage.NOT_ENOUGH_DATA_FOR_COURIER)
