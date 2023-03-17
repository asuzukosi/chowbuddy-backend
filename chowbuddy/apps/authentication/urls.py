from rest_framework.routers import SimpleRouter
from django.urls import path
from authentication.views import CustomBaseUserViewSet, CustomerTokenObtainPairView, RestaurantTokenObtainPairView, DelivererTokenObtainPairView


router = SimpleRouter()
router.register("users", CustomBaseUserViewSet)

urlpatterns = [
    path("login/customers", CustomerTokenObtainPairView.as_view(), name="login_customer"),
    path("login/restaurants", RestaurantTokenObtainPairView.as_view(), name="login_restaurant"),
    path("login/deliverer", DelivererTokenObtainPairView.as_view(), name="login_deliverer"),
] + router.urls