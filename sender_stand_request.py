import requests
import configuration
import data

#функция отправляет POST-запрос на создание заказа
def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=body,
        headers=data.headers
    )

#функция отправляет GET-запрос для получения заказа по номеру трека
def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER,
        params={"t": track},
        headers=data.headers
    )