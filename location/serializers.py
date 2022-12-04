from rest_framework import serializers
from .models import Location

class LocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'address', 'city', 'state')