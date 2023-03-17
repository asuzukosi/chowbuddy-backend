from delivery.views import DeliveryViewSet, DelivererViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'deliveries', DeliveryViewSet, basename="deliveries")
router.register(r'deliverers', DelivererViewSet, basename="deliverers")

urlpatterns = router.urls

