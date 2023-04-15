from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from restaurant.models import Restaurant, Dish


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class DishSerializer(ModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = Dish
        fields = "__all__"
    
