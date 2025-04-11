from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "date_joined",
        "id",
    )

    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")
