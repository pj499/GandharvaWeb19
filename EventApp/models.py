from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.

class MyUser(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'Participant'),
      (2, 'Event Head'),
      (3, 'Department Head'),
      (4, 'Joint Head'),
      (5, 'Gandharva Incharge'),
      (6, 'admin')
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default = 1)

  def __str__(self):
     return self.username

class EventMaster(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=100)
    num_of_winners = models.IntegerField()
    team_size = models.IntegerField()
    entry_fee = models.IntegerField()
    objective = models.CharField(max_length=1000)
    round1 = models.CharField(max_length=1000)
    round2 = models.CharField(max_length=1000)
    rules = models.CharField(max_length=1000)

    def __str__(self):
        return self.event_name

# model for Department


class Department(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    img = models.CharField(max_length=200)
    link_to = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EventDepartment(models.Model):
    event = models.ForeignKey(EventMaster, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class SponsorMaster(models.Model):
    sponsor_name = models.CharField(max_length=30)
    sponsor_logo = models.CharField(max_length=200)
    sponsor_info = models.CharField(max_length=200, default='No Info. Available')

    def __str__(self):
        return self.sponsor_name


class Carousel(models.Model):
    src = models.CharField(max_length=200)

class ContactUs(models.Model):
    user_name = models.CharField(max_length=30)
    user_id = models.EmailField()
    category = models.CharField(max_length = 100)
    user_message = models.CharField(max_length=300)

    def __str__(self):
        return self.user_name
