from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ['email', 'is_superuser', 'is_staff', 'is_active']
    list_filter = ['is_superuser', 'is_staff', 'is_active']
    search_fields = ['email']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ("permissions", {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        ("permissions", {
            "classes": ("wide", ),
            "fields": (
                'email', 'password1', 'password2', 'is_staff',
                'is_active', 'is_superuser',
            ),
        }),
        ("group permissions", {
            "fields": (
                "groups", "user_permissions",
            )
        }),
        ("important date", {
            "fields": (
                "last_login",
            )
        })
    )

admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)