from django.db import models
import datetime

# Create your models here.
class RequestType(models.Model):
    name = models.CharField(max_length=100)

class State(models.Model):
    name = models.CharField(max_length=100)

class Status(models.Model):
    status = models.CharField(max_length=100)

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=254)
    isValid = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)

class UserRequest(models.Model):
    request_type = models.TextField()
    request_desc = models.TextField()
    request_city = models.CharField(max_length=100)
    request_state = models.ForeignKey(State, on_delete=models.CASCADE)
    request_pincode = models.IntegerField()
    alternate_phone = models.CharField(max_length=20)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    remarks = models.TextField()
    updated_by = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    date_time = models.DateField(default=datetime.date.today)
