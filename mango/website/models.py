from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.validators import MinLengthValidator

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
    booking_flight = models.CharField(max_length=20, default=0)


class Payments(models.Model):
    # card_payment_id = models.ForeignKey(HotelUser, on_delete=models.CASCADE)
    card_num = models.CharField(max_length=16, validators=[MinLengthValidator(16, message="Card Number Must be 16 digits.")],blank=True)
    card_name = models.CharField(max_length=24,blank=True)
    card_cvc = models.CharField(max_length=3, validators=[MinLengthValidator(3, message="CVC has to be 3 digits")],blank=True)
    card_exp = models.DateField()