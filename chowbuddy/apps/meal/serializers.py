from rest_framework.serializers import ModelSerializer
from meal.models import Meal, DishOrder, MealOrder, MealPlan

class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"
        
class DishOrderSerializer(ModelSerializer):
    class Meta:
        model = DishOrder
        fields = "__all__"
        
class MealOrderSerializer(ModelSerializer):
    class Meta:
        model = MealOrder
        fields = "__all__"
        
class MealPlanSerializer(ModelSerializer):
    class Meta:
        model = MealPlan
        fields = "__all__"

    
