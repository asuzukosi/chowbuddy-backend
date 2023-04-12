from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from chowbuddy.utils.constants import USER_CATEGORIES
from customer.models import Customer
from restaurant.models import Restaurant
from delivery.models import Deliverer
from authentication.models import CustomUser


class CustomerTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom authentication token pair for customer users.
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        
        if not Customer.objects.filter(user=self.user).exists():
            raise Exception("Customer does not exist")
        
        customer:Customer = self.user.customer # This is the customer instance
        user = self.user 
        
        
        # restructure the customer token pair response to fit the requirements 
        # of the model
        data["id"] = customer.id
        data["user_id"] = user.id
        data["username"] = user.username
        data["email"] = user.email
        data["user"] = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        data["type"] = "customer"
        data["first_name"] = customer.first_name
        data["last_name"] = customer.last_name
        data["longitude"] = customer.longitude
        data["latitude"] = customer.latitude
        data["address"] = customer.address
        data["token"] = data["access"]
        
        
        del data["access"]
        del data["refresh"]
        
        return data

class RestaurantTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom authentication for Restuarant
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        
        if not Restaurant.objects.filter(user=self.user).exists():
            raise Exception("Restaurant does not exist")
        
        restuarant:Restaurant = self.user.restaurant
        user = self.user
        
        data["id"] = restuarant.id
        data["user_id"] = user.id
        data["name"] = restuarant.name
        data["address"] = restuarant.address
        data["phone"] = restuarant.phone
        data["image"] = restuarant.image
        data["long"] = restuarant.long
        data["lat"] = restuarant.lat
        data["token"] = data["access"]
        
        del data["access"]
        del data["refresh"]
        
        return data
        

class DelivererTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom authentication for Deliverer
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        
        if not Deliverer.objects.filter(user=self.user).exists():
            raise Exception("Deliverer does not exist")
        
        deliverer:Deliverer = self.user.deliverer
        user = self.user
        
        data["id"] = deliverer.id
        data["user_id"] = user.id
        data["email"] = user.email 
        data["username"] = user.username
        data["location"] = deliverer.location
        data["token"] = data["access"]
        
        del data["access"]
        del data["token"]
        
        return data
    
class CustomBaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]






