from django.contrib import admin
from django.urls import include, path

import backend.authentication.urls
import backend.users.urls.api_urls
import backend.users.urls.simple_urls

API_PREFIX = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(backend.authentication.urls)),
    path('users/', include(backend.users.urls.simple_urls)),
    path(API_PREFIX, include(backend.users.urls.api_urls)),
]
