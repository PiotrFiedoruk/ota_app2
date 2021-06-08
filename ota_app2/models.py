import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

# refer to extended User model as settings.AUTH_USER_MODEL when using foreignkey
class User(AbstractUser):
    nickname = models.CharField(max_length=50)

CLX_CHOICES = ((1, 'Percentage'),
               (2, 'Nights'),
               (3, 'Fixed'))


class Cancellation(models.Model):
    name = models.CharField(max_length=50)
    type = MultiSelectField(choices=CLX_CHOICES)
    penalty1 = models.IntegerField()
    time1 = models.IntegerField()
    penalty2 = models.IntegerField()
    time2 = models.IntegerField()

class Hotel(models.Model):
    owner = models.ManyToManyField(User, related_name='owners')
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}  ({str(self.id)})'


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    occ_adult = models.IntegerField()
    occ_child = models.IntegerField()

    def __str__(self):
        return f'{self.name}  ({str(self.id)}) - {self.hotel.name}'


class Rateplan(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rateplans')
    name = models.CharField(max_length=30)
    cancellation = models.ForeignKey(Cancellation, on_delete=models.CASCADE, related_name='clx')
    # check cascade here

class Price(models.Model):
    rateplan = models.ForeignKey(Rateplan, on_delete=models.CASCADE, related_name='prices')
    date = models.DateField(null=True)
    availability = models.SmallIntegerField()
    price_1 = models.DecimalField(max_digits=8, decimal_places=2)
    price_2 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_3 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_4 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_5 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_6 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_7 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_8 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_9 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_10 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_11 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    price_12 = models.DecimalField(max_digits=8, decimal_places=2, null=True)

class Availablity(models.Model):
    pass