from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from insights.models import AssetInteraction, TimeInteraction


class AssetInteractionInline(admin.StackedInline):
    model = AssetInteraction


class TimeInteractionInline(admin.StackedInline):
    model = TimeInteraction


class UserAdmin(BaseUserAdmin):
    inlines = [
        AssetInteractionInline,
        TimeInteractionInline,
    ]


admin.site.register(User, UserAdmin)
