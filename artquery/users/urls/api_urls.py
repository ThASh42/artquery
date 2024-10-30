from rest_framework.routers import SimpleRouter

from ..views.users import UserViewSet

app_name = "api_users"

router = SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
