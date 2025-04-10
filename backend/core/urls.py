from django.contrib import admin
from django.urls import include, path

import backend.authentication.urls
import backend.authentication.api.v1.urls
import backend.users.urls.api_urls
import backend.users.urls.web_urls

API_PREFIX = "api/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include(backend.authentication.urls)),
    path("users/", include(backend.users.urls.web_urls)),
    path(f"{API_PREFIX}users/", include(backend.users.urls.api_urls)),
    path(f"{API_PREFIX}auth/", include(backend.authentication.api.v1.urls)),
]
