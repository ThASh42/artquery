from django.contrib import admin
from django.urls import include, path

import artquery.users.urls
from artquery.authentication.views.login import LoginView

API_PREFIX = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(), name='login'),
    path(API_PREFIX, include(artquery.users.urls)),
]
