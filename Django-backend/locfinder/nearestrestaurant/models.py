from django.db import models

# Create your models here.

class Place(models.Model):
    place_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    place_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)
    price_level=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    num_ratings=models.CharField(max_length=200)
    query_place_id=models.CharField(max_length=200)
    food_style=models.CharField(max_length=200)
    food_type=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RestaurantType(models.Model):
    type=models.CharField(max_length=200)
    avg_rating=models.CharField(max_length=200)
    avg_num_ratings=models.CharField(max_length=200)
    number=models.CharField(max_length=200)

    def __str__(self):
        return self.type
    
class GMapDetail(models.Model):
    place_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    hours=models.CharField(max_length=1000)
    price_level=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    num_ratings=models.CharField(max_length=200)
    r1_name=models.CharField(max_length=200)
    r1_score=models.CharField(max_length=200)
    r1_text=models.CharField(max_length=1000)
    r2_name=models.CharField(max_length=200)
    r2_score=models.CharField(max_length=200)
    r2_text=models.CharField(max_length=1000)
    r3_name=models.CharField(max_length=200)
    r3_score=models.CharField(max_length=200)
    r3_text=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class YelpDetail(models.Model):
    place_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
    price_level=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    num_ratings=models.CharField(max_length=200)
    r1_name=models.CharField(max_length=200)
    r1_score=models.CharField(max_length=200)
    r1_text=models.CharField(max_length=1000)
    r2_name=models.CharField(max_length=200)
    r2_score=models.CharField(max_length=200)
    r2_text=models.CharField(max_length=1000)
    r3_name=models.CharField(max_length=200)
    r3_score=models.CharField(max_length=200)
    r3_text=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

