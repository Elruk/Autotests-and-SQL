# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}
# данные пользователя для создания нового заказа
user_order = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Центральный",
            "metroStation": 204,
            "phone": "+34916123451",
            "rentTime": 5,
            "deliveryDate": "2026-06-24",
            "color": ["BLACK"],
            "comment": "test"
        }