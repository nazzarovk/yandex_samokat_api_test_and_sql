# Кирилл Назаров, 15-я когорта - Финальный проект. Инжененер по тестированию плюс.

import sender_stand_request
import data

def get_new_order_track():
    body = data.order_body
    track = sender_stand_request.post_new_order(body).json()["track"]
    return track


def test_get_order_data_by_track_success_response():
    track = get_new_order_track()
    get_order_response = sender_stand_request.get_order_by_track(track)

    assert get_order_response.status_code == 200