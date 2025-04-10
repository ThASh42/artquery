from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views.token import CookieTokenRefreshView
from .views.login import LoginAPIView


app_name = "api_authentication"

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('v1/login/', LoginAPIView.as_view(), name='login'),
]
