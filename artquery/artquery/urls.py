from django.contrib import admin
from django.urls import include, path

import artquery.authentication.urls
import artquery.users.urls.api_urls
import artquery.users.urls.simple_urls

API_PREFIX = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(artquery.authentication.urls)),
    path('users/', include(artquery.users.urls.simple_urls)),
    path(API_PREFIX, include(artquery.users.urls.api_urls)),
]
