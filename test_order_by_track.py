import data
import sender_stand_request

def test_get_order_by_track():
    #Выполнение запрос на создание заказа
    create_response = sender_stand_request.post_new_order(data.user_order)
    assert create_response.status_code == 201

    #Сохранение номера трека заказа
    track = create_response.json()["track"]

    # Выполнение запроса на получение заказа по треку заказа
    get_response = sender_stand_request.get_order_by_track(track)
    
    #код ответа должен быть равен 200
    assert get_response.status_code == 200