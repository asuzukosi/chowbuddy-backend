from rest_framework.serializers import ModelSerializer
from restaurant.models import Restaurant, Dish


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"
