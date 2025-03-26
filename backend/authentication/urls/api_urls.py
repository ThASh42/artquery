from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from ..views.token import CookieTokenRefreshView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
]
