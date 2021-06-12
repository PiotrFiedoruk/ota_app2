import pytest
from django.test import Client
from ota_app2.models import Hotel, Room, Rateplan, Price, Cancellation, User

@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def client_auth():
    user = User.objects.create_user(username='zenon@zenon', password='zenon')
    client.force_login(user)
    return client

@pytest.fixture
def standard_user():
    standard_user = User.objects.create_user(username='zenon@zenon', password='zenon')
    return standard_user

@pytest.fixture
def hotel():
    standard_user = User.objects.create_user(username='zenon@zenon', password='zenon')
    hotel = Hotel.objects.create(name='Hilton', city='Warsaw')
    hotel.owner.add(standard_user)
    return hotel

@pytest.fixture
def room(hotel):
    room = Room.objects.create(name='Double', occ_adult=2, occ_child=2, hotel=hotel)
    return room

@pytest.fixture
def canlcellation(room):
    cancellation = Cancellation.objects.create(name='Standard', penalty1=10, time1=24, penalty2=10, time2=24)
    return cancellation

@pytest.fixture
def rateplan(room, canlcellation):
    rateplan = Rateplan.objects.create(name='Standard', room=room, cancellation=canlcellation)
    return rateplan

