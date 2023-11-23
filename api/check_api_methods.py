import allure
from data import Profile


class CheckMethods:
    @staticmethod
    @allure.step("Проверка status_code ответа")
    def check_status_code(response, code):
        assert response.status_code == code, (f"Возвращенный status_code не соответствует. Ожидаемый: {code}, "
                                              f"фактический: {response.status_code}")

    @staticmethod
    @allure.step("Проверка текста ответа на запрос")
    def check_text_message(response, text):
        assert response.text == text, (f"Ответ не соответствует ожидаемому, ожидалось: {text}, фактический ответ: "
                                       f"{response.text}")

    @staticmethod
    @allure.step("Проверка json-ответа по ключу 'message'")
    def check_json_message(response, text):
        assert response.json()['message'] == text, (f"Ответ не соответствует ожидаемому, ожидалось: {text}, "
                                                    f"фактический ответ: {response.json()['message']}")

    @staticmethod
    @allure.step("Проверка наличия ключа в json-ответе")
    def check_text_in_json(response, text):
        assert text in response.json(), f"{text} отсутствует в теле ответа"

    @staticmethod
    @allure.step("Проверка соответствия ID курьера в json-ответе фактическому ID")
    def check_json_id(response):
        assert response.json()['id'] == Profile.ID, (f"Запрос не вернул ID или вернул некорректный ID, ожидаемый ID: "
                                                     f"{Profile.ID}, фактический ID: {response.json()['id']}")

    @staticmethod
    @allure.step("Проверка наличия списка заказов по ключу 'orders' в json-ответе")
    def check_orders_list(response):
        assert isinstance(response.json()['orders'], list), "В тело ответа не возвращается список заказов."
