from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from ota_app2.models import User, Hotel, Room, Rateplan, Price
from ota_app2.serializers import UserSerializer, HotelSerializer, RoomSerializer, RateplanSerializer, PriceSerializer
from rest_framework import viewsets, filters


class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HotelApiView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all().distinct()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'name':['contains'], 'city':['contains'], 'rooms__occ_adult':['gte'],
                        'rooms__occ_child':['gte'], 'rooms__rateplans__prices__availability':['gte'],
                        'rooms__rateplans__prices__date':['gte', 'lte']}
    search_fields = ['name', 'city', 'rooms__rateplans__name']
    ordering_fields = ['name', 'city']
    ordering = ['name']


class RoomApiView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'hotel':['exact'], 'hotel__city':['contains'], 'name':['exact'],
                        'occ_adult':['gte'], 'occ_child':['gte'], 'rateplans__prices__availability':['gte'],
                        'rateplans__prices__date':['gte', 'lte']}
    search_fields = ['name', 'city']
    ordering_fields = ['name', 'city']
    ordering = ['name']


class RateplanApiView(viewsets.ModelViewSet):
    queryset = Rateplan.objects.all()
    serializer_class = RateplanSerializer

class PriceApiView(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer











    #
    # # define custom queryset (remove queryset variable from the top of the class)
    # def get_queryset(self):
    #     return User.objects.all()
    #
    #
    # custom get object by name
    # def get_object(self, queryset=None, **kwargs):
    #     user_id = self.kwargs.get('pk')
    #     return get_object_or_404(User, username=user_id)
    #
    #
    # custom classes in case of (viewsets.Viewset) inheritance
    # def list(self, request):
    #     serializer_class = UserSerializer(self.queryset, many=True)
    #     return Response(serializer_class.data)
    #
    # def create(self, request):
    #     pass
    #
    # def retrieve(self, request, pk=None):
    #     post = get_object_or_404(self.queryset, pk=pk)
    #     serializer_class = UserSerializer(post)
    #     return Response(serializer_class.data)
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass
    #
    # h = Hotel.objects.filter(rooms__rateplans__prices__date__range=['2021-6-8', '2021-6-9']).filter(
    #     rooms__rateplans__prices__availability__gt=0).distinct()