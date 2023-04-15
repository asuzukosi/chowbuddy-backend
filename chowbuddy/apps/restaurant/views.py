from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from restaurant.models import Restaurant, Dish
from restaurant.serializers import RestaurantSerializer, DishSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["name", "categories"]
    ordering_fields = ["name"]
    search_fields = ["description", "name",]
    
    @action(methods=["get"], detail=True)
    def dishes(self, request, pk,  *args, **kwargs):
        restaurant = Restaurant.objects.get(id=pk)
        dishes = Dish.objects.filter(restaurant=restaurant)
        serializer = DishSerializer(instance=dishes, many=True)
        return Response(serializer.data, 200)
        
class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["restaurant"]
    ordering_fields = ["restaurant"]
    search_fields = ["name"]