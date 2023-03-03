from rest_framework.routers import DefaultRouter
from meal.views import MealViewset, MealPlanViewset, MealOrderViewset, DishOrderViewset

router = DefaultRouter()
router.register('meals', MealViewset, basename='meals')
router.register('mealplans', MealPlanViewset, basename='mealplans')
router.register('mealorders', MealOrderViewset, basename='mealorders')
router.register('dishorders', DishOrderViewset, basename='dishorders')

urlpatterns = router.urls