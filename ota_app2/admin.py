from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Hotel, Price, Cancellation, Rateplan, Room

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Rateplan)
admin.site.register(Price)
admin.site.register(Cancellation)