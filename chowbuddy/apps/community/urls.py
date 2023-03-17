from rest_framework.routers import SimpleRouter
from community.views import CommunityViewSet, PostViewSet

router = SimpleRouter()
router.register(r'communities', CommunityViewSet, basename="communities")
router.register(r'posts', PostViewSet, basename="posts")

urlpatterns = router.urls