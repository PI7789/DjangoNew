from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class HotelUser(AbstractUser):
    phonenum = models.CharField(max_length=14, blank=True) 

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, editable=False)
    booking_user_id = models.ForeignKey(HotelUser, on_delete=models.CASCADE)
    booking_VIP_status = models.CharField(default = "", max_length=10)
    booking_startdate = models.DateField()
    booking_enddate = models.DateField()
    booking_people = models.IntegerField(default=0)
    booking_cost = models.FloatField(default=0)
