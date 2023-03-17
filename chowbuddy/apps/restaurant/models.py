from django.db import models
from django.contrib.auth import get_user_model

class RestaurantManager(models.Manager):
    def create(self,*args, **kwargs):
        username = kwargs["name"].lower().replace(" ","")
        if get_user_model().objects.filter(username=username).exists():
            user = get_user_model().objects.get(username=username)
            
        elif get_user_model().objects.filter(email=kwargs["email"]).exists():
            user = get_user_model().objects.get(email=kwargs["email"])
        
        else:
            user = get_user_model().objects.create(username=username, email=kwargs["email"], is_active=True, password=username)
            user.set_password(username)
            user.save()

        return super(RestaurantManager, self).create(user=user, *args, **kwargs)

class Restaurant(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="restaurant")    
    name = models.CharField(max_length=1000)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField()
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='restaurant_images')
    long = models.FloatField()
    lat = models.FloatField()
    rating = models.FloatField()
    ranking = models.CharField(max_length=1000)
    price_level = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = RestaurantManager()
    
    
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
    
    

