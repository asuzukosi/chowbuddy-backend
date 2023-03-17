from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    friends = models.ManyToManyField("Customer", blank=True, related_name="friendships")
    
    