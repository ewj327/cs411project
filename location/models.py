from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=240)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)

    def _str_(self):
        return self.name