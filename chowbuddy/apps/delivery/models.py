from django.db import models
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant
from customer.models import Customer
# Create your models here.
class Deliverer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="deliverer")
    location = models.CharField(max_length=100)

class Delivery(models.Model):
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurantLocation = models.CharField(max_length=100)
    customerLocation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(auto_now=True)
    
