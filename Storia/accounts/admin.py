from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# from insights.admin import AwardanceInline
from insights.models import AssetInteraction, TimeInteraction


class AssetInteractionInline(admin.StackedInline):
    model = AssetInteraction


class TimeInteractionInline(admin.StackedInline):
    model = TimeInteraction


class UserAdmin(BaseUserAdmin):
    inlines = [
        # AssetInteractionInline,
        # TimeInteractionInline,
        # AwardanceInline
    ]

    filter_horizontal = ('merits',)


admin.site.register(User, UserAdmin)
# admin.site.register(Profile)