import pytest
from conftest import client, client_auth, room, standard_user

@pytest.mark.django_db
def test_room_list(client):
    response = client.get('/api/rooms/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_hotel_list(client):
    response = client.get('/api/hotels/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_hotel_list_response(client, hotel):
    response = client.get('/api/hotels/')
    print(response.content)
    assert len(response.json()) == 1

@pytest.mark.django_db
def test_room_list_response(client, room):
    response = client.get('/api/rooms/')
    print(response.content)
    assert len(response.json()) == 1

@pytest.mark.django_db
def test_hotel_list_response_filter_by_name_correct(client, hotel):
    response = client.get('/api/hotels/?name__contains=Hi')
    assert len(response.json()) == 1

@pytest.mark.django_db
def test_hotel_list_response_filter_by_name_incorrect(client, hotel):
    response = client.get('/api/hotels/?name__contains=wa')
    assert len(response.json()) == 0

@pytest.mark.django_db
def test_hotel_list_response_filter_by_city_correct(client, hotel):
    response = client.get('/api/hotels/?city__contains=Wa')
    assert len(response.json()) == 1

@pytest.mark.django_db
def test_hotel_list_response_filter_by_city_incorrect(client, hotel):
    response = client.get('/api/hotels/?city__contains=asda')
    assert len(response.json()) == 0

@pytest.mark.django_db
def test_hotel_list_response_filter_by_room_adult_occ_correct(client, hotel, room):
    hotel.rooms.add(room)
    response = client.get('/api/hotels/?rooms__occ_adult__gte=1')
    assert len(response.json()) == 1

@pytest.mark.django_db
def test_hotel_list_response_filter_by_room_adult_occ_incorrect(client, hotel):
    response = client.get('/api/hotels/?rooms__occ_adult__gte=12')
    assert len(response.json()) == 0

@pytest.mark.django_db
def test_rateplan_list_response_correct(client, rateplan):
    response = client.get('/api/rateplans/')
    print(response.content)
    assert len(response.json()) == 1

