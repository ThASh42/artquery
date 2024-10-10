# from artquery.authentication.views.login import LoginView
from django.contrib import admin
from django.urls import include, path

import artquery.accounts.urls

API_PREFIX = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login', LoginView.as_view(), name='login'),
    path(API_PREFIX, include(artquery.accounts.urls)),
]
