from customer.views import CustomerViewSet, FriendshipViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename="customers")
router.register(r'friendships', FriendshipViewSet, basename="friendships")



urlpatterns = router.urls
