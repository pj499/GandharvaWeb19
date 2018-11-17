from django.db import models

# Create your models here.
class EventMaster(models.Model):
    event_id = models.CharField(unique = True)
    event_name = models.CharField(max_length=100)
    num_of_winners = models.IntegerField()
    team_size = models.IntegerField()
    entry_fee = models.IntegerField()
    rules = models.CharField()

# model for Department
class Department(models.Model):
    dep_id = models.CharField(unique = True)
    name = models.CharField()

class EventDepartment(models.Model):
    event_dep_id = models.CharField(unique = True )
    event = models.ForeignKey(EventMaster.event_id ,on_delete = models.CASCADE)
    department = models.ForeignKey(Department.dep_id , on_delete=models.CASCADE)
