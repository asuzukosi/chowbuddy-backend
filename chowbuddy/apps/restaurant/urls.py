from restaurant.views import RestaurantViewSet, DishViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('dishes', DishViewSet)

urlpatterns = router.urls
