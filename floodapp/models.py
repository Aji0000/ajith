from django.db import models

# Create your models here.
class Users(models.Model):
    Name=models.CharField(max_length=30)
    EmailID=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    PhoneNo=models.BigIntegerField()
class Camps(models.Model):
    Pic=models.ImageField(upload_to='static/assets/images/camps/')
    Place=models.CharField(max_length=30)
    Avalilability=models.CharField(max_length=30)