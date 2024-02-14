# In your Django app's admin.py file

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post
from reversion.admin import VersionAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin, VersionAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_active', 'created_at', 'updated_at')
    search_fields = ('email', 'username')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
@admin.register(Post)
class PostModelAdmin(VersionAdmin):
    pass