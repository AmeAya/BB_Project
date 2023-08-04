from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'name', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password', 'date_joined')}),
        ("Permissions", {'fields': (
            'is_staff', 'is_active', 'is_superuser'
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'
            )
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email', 'name')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
