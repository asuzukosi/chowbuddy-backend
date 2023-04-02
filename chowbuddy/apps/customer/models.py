from django.db import models
from django.contrib.auth import get_user_model
from community.models import Community

# Create your models here.

class CustomerManager(models.Manager):
    def create(self, username:str, email:str, password:str,*args,  **kwargs):
        if get_user_model.objects.filter(username=username, email=email).exists():
            raise Exception('Customer already exists')
        user = get_user_model().objects.create(username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        return super().create(user=user, email=email,*args, **kwargs)


class Customer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="customer")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    friends = models.ManyToManyField("Customer", blank=True, related_name="friendships")
    longitude = models.FloatField(default=0.0, blank=True, null=True)
    latitude = models.FloatField(default=0.0, blank=True, null=True)
    
    
    objects = CustomerManager()
    
    def __str__(self):
        return self.user
    
    def getMyCommunities(self):
        return self.user.community_members.all()
    
    def getSuggestedCommunites(self):
        allCommunites = Community.objects.all()
        suggestedCommunities = [community for community in allCommunites if community not in self.user.community_members.all()]
        return suggestedCommunities
    
    def setLongLat(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
        self.save()
        
    def getMealPlans(self):
        return self.user.meal_plans.all()
    
    