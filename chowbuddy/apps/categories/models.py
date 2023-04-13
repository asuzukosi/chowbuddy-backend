from django.db import models
from restaurant.models import Restaurant

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    restaurants = models.ManyToManyField(Restaurant, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.name