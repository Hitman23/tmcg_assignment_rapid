from django.db import models


# Create your models here.

class GetData(models.Model):
    url = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    number_of_groups = models.IntegerField(default=0)

    def __str__(self):
        return self.url


class Groups(models.Model):
    name = models.CharField(max_length=100)
    number_of_contacts = models.IntegerField(default=0)

    def __str__(self):
        return self.name
