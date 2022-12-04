from django.contrib import admin
from .models import Location

class LocAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state')

# Register your models here.

admin.site.register(Location, LocAdmin)