from rest_framework import serializers
from ota_app2.models import User, Hotel, Room, Rateplan, Price, Cancellation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ['url', 'id', 'name', 'city', 'owner', 'rooms']
        read_only_fields = ['owner']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['url', 'id', 'hotel', 'name', 'occ_adult', 'occ_child', 'rateplans']
        read_only_fields = ['rateplans']

class RateplanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rateplan
        fields = ['url', 'id', 'room', 'name', 'prices', 'room']
        read_only_fields = ['prices', 'room']

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['url', 'id', 'rateplan', 'date', 'availability', 'price_1', 'price_2', 'price_3', 'price_4',
                  'price_5', 'price_6', 'price_7', 'price_8', 'price_9', 'price_10', 'price_11', 'price_12']

class CancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancellation
        fields = '__all__'
#
