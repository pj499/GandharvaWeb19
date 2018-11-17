from django.db import models

# Create your models here.


class SponsorMaster(models.Model):
    sponsor_id = models.IntegerField(primary_key=True)
    sponsor_name = models.CharField(max_length=30)
    sponsor_logo = models.CharField(max_length=200)
    sponsor_info = models.CharField(max_length=200, default='No Info. Available')

    def __str__(self):
        return self.sponsor_name


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class SponsorCategory(models.Model):
    sponsor_id = models.ForeignKey(SponsorMaster, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)


