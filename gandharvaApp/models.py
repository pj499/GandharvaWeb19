from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length = 50)
    password = models.CharField(max_length= 200)
    role = models.CharField(max_length = 5)
    phone = models.IntegerField()
    email = models.CharField(max_length = 80)

# to add remainging tables