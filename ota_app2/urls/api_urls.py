from django.urls import path
from ota_app2.views.api_views import UserApiView, HotelApiView, RoomApiView, RateplanApiView, PriceApiView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserApiView, basename='user')
router.register('hotels', HotelApiView, basename='hotel')
router.register('rooms', RoomApiView, basename='room')
router.register('rateplans', RateplanApiView, basename='rateplan')
router.register('prices', PriceApiView, basename='price')

urlpatterns = router.urls

