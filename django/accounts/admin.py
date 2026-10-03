from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AuthIdentity, User


@admin.register(User)
class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'display_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'display_name')


@admin.register(AuthIdentity)
class AuthIdentityAdmin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'linked_at')
    search_fields = ('user__username', 'provider_subject')
    readonly_fields = ('linked_at',)
