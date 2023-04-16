from rest_framework.serializers import ModelSerializer
from meal.models import Meal, DishOrder, MealOrder, MealPlan
from rest_framework import serializers
from restaurant.serializers import DishSerializer
class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"
        
class DishOrderSerializer(ModelSerializer):
    class Meta:
        model = DishOrder
        fields = "__all__"
        
class DishOrderFullSerializer(ModelSerializer):
    dish = DishSerializer()
    class Meta:
        model = DishOrder
        fields = "__all__"

class MealFullSerializer(ModelSerializer):
    dish_orders = DishOrderFullSerializer(many=True)
    class Meta:
        model = Meal
        fields = "__all__"
        
class MealOrderSerializer(ModelSerializer):
    class Meta:
        model = MealOrder
        fields = "__all__"
        
class MealOrderFullSerializer(ModelSerializer):
    meal = MealFullSerializer()
    class Meta:
        model = MealOrder
        fields = "__all__"
        
class MealPlanSerializer(ModelSerializer):
    class Meta:
        model = MealPlan
        fields = "__all__"


class DishOrderSerializer(serializers.Serializer):
    dish = serializers.IntegerField()
    quantity = serializers.IntegerField()
    amount = serializers.FloatField()
    

class CreateOrderSerializer(serializers.Serializer):
    restaurant = serializers.IntegerField()
    dishorders = serializers.ListField(child=DishOrderSerializer())
    deliverer =  serializers.IntegerField()
    customer = serializers.IntegerField()
    
    
class GetCustomerOrders(serializers.Serializer):
    customerId = serializers.IntegerField()
    
    
class GetRestaurantOrders(serializers.Serializer):
    restaurantId = serializers.IntegerField()
    
