from django.db import models
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant
from customer.models import Customer
# Create your models here.
class DelivererManager(models.Manager):
    def create(self,username, email,password,*args,**kwargs):
        if get_user_model().objects.filter(username=username, email=email).exists():
            raise Exception('User already exists')
        user = get_user_model().objects.create(username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        
        return super().create(user, **kwargs)
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
    
