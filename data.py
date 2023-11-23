class URLS:
    ENDPOINT_CREATE_OR_DELETE_COURIER = "http://qa-scooter.praktikum-services.ru/api/v1/courier"
    ENDPOINT_LOGIN = "http://qa-scooter.praktikum-services.ru/api/v1/courier/login"
    ENDPOINT_CREATE_OR_GET_ORDER = "http://qa-scooter.praktikum-services.ru/api/v1/orders"
    ENDPOINT_ACCEPT_ORDER = "http://qa-scooter.praktikum-services.ru/api/v1/orders/accept/"
    ENDPOINT_GET_ORDER_BY_TRACK = "http://qa-scooter.praktikum-services.ru/api/v1/orders/track"
    ENDPOINT_CANSEL_ORDER = "http://qa-scooter.praktikum-services.ru/api/v1/orders/cancel"
    ENDPOINT_FINISH_ORDER = "http://qa-scooter.praktikum-services.ru/api/v1/orders/finish/"


class Profile:
    LOGIN = "alex_sh"
    LOGIN_WRONG = 'alex_shl'
    PASSWORD = "1234567"
    PASSWORD_WRONG = '12345'
    ID = 235472
    WRONG_ID = 999999999


class Order:
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

    BLACK_COLOR = ["BLACK"]
    GREY_COLOR = ["GREY"]
    BOTH_COLOR = ["BLACK, GREY"]
    WRONG_TRACK = 999999999
    EMPTY_DATA = ""
    ORDER_ID = 681999
    ORDER_WRONG_ID = 9999999


class StatusCode:
    CODE_201 = 201
    CODE_409 = 409
    CODE_400 = 400
    CODE_404 = 404
    CODE_200 = 200


class TextMessage:
    TRUE_MESSAGE = '{"ok":true}'
    LOGIN_ALREADY_USE = "Этот логин уже используется. Попробуйте другой."
    NOT_ENOUGH_DATA_FOR_COURIER = "Недостаточно данных для создания учетной записи"
    NOT_ENOUGH_DATA_FOR_LOGIN = "Недостаточно данных для входа"
    NO_PROFILE = "Учетная запись не найдена"
    NO_COURIER_IDENT = f"Курьер с идентификатором {Profile.WRONG_ID} не найден"
    NO_COURIER_ID = "Курьера с таким id нет."
    NO_COURIER_ID_EXIST = "Курьера с таким id не существует"
    TRACK = 'track'
    ORDER = "order"
    NOT_FOUND = "Not Found."
    TRACK_NOT_FOUND = "Заказ не найден"
    NOT_ENOUGH_DATA_FOR_SEARCH = "Недостаточно данных для поиска"
    NO_ORDER_ID = "Заказа с таким id не существует"
