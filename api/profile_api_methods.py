import allure
import requests
from faker import Faker
from data import URLS


class ProfileMethods:
    @staticmethod
    @allure.step("Создаем логин и пароль для профиля курьера")
    def courier_generate_profile():
        fake = Faker()
        profile = {"login": fake.user_name(),
                   "password": fake.password()}
        return profile

    @staticmethod
    @allure.step("Создание курьера")
    def create_courier():
        payload = ProfileMethods.courier_generate_profile()
        response = requests.post(URLS.ENDPOINT_CREATE_OR_DELETE_COURIER, data=payload)
        return response, payload

    @staticmethod
    @allure.step("Логин курьера в систему, возврат ID курьера")
    def login_courier(profile):
        response_login = requests.post(URLS.ENDPOINT_LOGIN, data=profile)
        return response_login.json()['id']