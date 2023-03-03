from django.db import models
from restaurant.models import Dish, Restaurant
from customer.models import Customer
from delivery.models import Delivery
# Create your models here.

class DishOrder(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
class Meal(models.Model):
    dish_orders =  models.ManyToManyField(DishOrder)
    restaurants = models.ManyToManyField(Restaurant)

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    meal =  models.ForeignKey(Meal, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customers = models.ManyToManyField(Customer)
    next_interval = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MealOrder(models.Model):
     meal =  models.ForeignKey(Meal, on_delete=models.CASCADE)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     status = models.CharField(max_length=100)
     delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
