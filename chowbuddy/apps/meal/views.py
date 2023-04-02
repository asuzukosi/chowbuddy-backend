from django.shortcuts import render
from meal.serializers import MealSerializer, DishOrderSerializer, MealOrderSerializer, MealPlanSerializer, CreateOrderSerializer, GetCustomerOrders, GetRestaurantOrders
from meal.models import Meal, DishOrder, MealOrder, MealPlan
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class MealViewset(ModelViewSet):
    queryset =  Meal.objects.all()
    serializer_class = MealSerializer
    
    
class DishOrderViewset(ModelViewSet):
    queryset = DishOrder.objects.all()
    serializer_class = DishOrderSerializer
    
    
class MealOrderViewset(ModelViewSet):
    queryset = MealOrder.objects.all()
    serializer_class = MealOrderSerializer
    
    @action(methods=["post"], detail=False)
    def create_order(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = MealOrder.create_order(**serializer)
        serializer = MealOrderSerializer(instance=order)
        return Response(serializer.data, 200)
    
    @action(methods=["post"], detail=False)
    def get_customers_orders(self, request, *args, **kwargs):
        serializer = GetCustomerOrders(data=request.data)
        serializer.is_valid(raise_exception=True)
        orders = MealOrder.getAllOrdersForCustomer(**serializer.data)
        serializer = MealOrderSerializer(instance=orders, many=True)
        return Response(serializer.data, 200)
            
    @action(methods=["post"], detail=False)
    def get_restaurants_orders(self, request, *args, **kwargs):
        serializer = GetRestaurantOrders(data=request.data)
        serializer.is_valid(raise_exception=True)
        orders = MealOrder.getAllOrdersFromRestaurant(**serializer.data)
        serializer = MealOrderSerializer(instance=orders, many=True)
        return Response(serializer.data, 200)

class MealPlanViewset(ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer
    