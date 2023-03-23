from django.contrib import admin
from meal.models import DishOrder, Meal, MealPlan, MealOrder

# Register your models here.
admin.site.register(DishOrder)
admin.site.register(MealOrder)
admin.site.register(Meal)
admin.site.register(MealPlan)
