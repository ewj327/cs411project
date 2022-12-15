from django.contrib import admin
from . import models

admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.RestaurantType)
admin.site.register(models.GMapDetail)
admin.site.register(models.YelpDetail)
