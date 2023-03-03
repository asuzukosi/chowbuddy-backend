from django.shortcuts import render
from meal.serializers import MealSerializer, DishOrderSerializer, MealOrderSerializer, MealPlanSerializer
from meal.models import Meal, DishOrder, MealOrder, MealPlan
from rest_framework.viewsets import ModelViewSet


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
    

class MealPlanViewset(ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer
    