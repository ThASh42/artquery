from rest_framework.routers import DefaultRouter

from ..views.users import UserViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'', UserViewSet, basename='api_users')
urlpatterns = router.urls
