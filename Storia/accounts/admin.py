from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from insights.admin import AwardanceInline
from insights.models import AssetInteraction, TimeInteraction

from .models import User, Merit, Awardance, Profile


class AssetInteractionInline(admin.StackedInline):
    model = AssetInteraction


class TimeInteractionInline(admin.StackedInline):
    model = TimeInteraction


class AwardanceInline(admin.StackedInline):
    model = Awardance


# class MeritInline(admin.StackedInline):
#     model = Merit


class UserAdmin(BaseUserAdmin):
    inlines = [
        # AssetInteractionInline,
        # TimeInteractionInline,
        AwardanceInline
    ]

    # filter_horizontal = ('merits',)


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Merit)
admin.site.register(Awardance)
