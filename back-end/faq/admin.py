from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'user_type', 'is_staff')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Permissions', {'fields': ('user_type', 'is_active')}),
#     )

admin.site.register(User)