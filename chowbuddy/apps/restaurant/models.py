from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Restaurant(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurant_images')
    long = models.FloatField()
    lat = models.FloatField()
    
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='dish_images')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.restaurant} -> {self.name} + {self.price}"
    

# class Review(models.Model):
#     dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    
    

