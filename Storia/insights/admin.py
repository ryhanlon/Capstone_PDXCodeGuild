from django.contrib import admin

from .models import Interaction, AssetInteraction, TimeInteraction

admin.site.register(Interaction)
admin.site.register(AssetInteraction)
admin.site.register(TimeInteraction)
