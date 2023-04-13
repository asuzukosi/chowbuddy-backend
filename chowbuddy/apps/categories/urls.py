from rest_framework.routers import SimpleRouter
from django.urls import path
from categories.views import CategoryViewSet



router = SimpleRouter()
router.register("category", CategoryViewSet, basename="category")

urlpatterns = router.urls