from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from restaurant.models import Restaurant, Dish
from restaurant.serializers import RestaurantSerializer, DishSerializer


# Create your views here.
class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer