from django.db import models


# Create your models here.
class Users(models.Model):
    Fullname = models.CharField(max_length=50)
    Username = models.CharField(max_length=50)
    Email = models.EmailField( max_length=254)
    PhoneNumber = models.PositiveIntegerField()
    Password = models.CharField( max_length=50)
    gender = models.CharField(max_length=10)
