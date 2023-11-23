import requests
import allure
import json
from data import URLS, Order


class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа и получение track номера")
    def create_order_and_get_track():
        payload = Order.order_data
        response = requests.post(URLS.ENDPOINT_CREATE_OR_GET_ORDER, data=json.dumps(payload))
        return response.json()['track']

    @staticmethod
    @allure.step("Получение ID заказа по track номеру")
    def get_order_id_by_track(track_id):
        params = {"t": track_id}
        response = requests.get(URLS.ENDPOINT_GET_ORDER_BY_TRACK, params=params)
        return response.json()['order']['id']


