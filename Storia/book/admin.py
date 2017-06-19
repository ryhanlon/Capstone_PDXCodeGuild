from django.contrib import admin
from .models import Media, MediaImage, Book, Interaction

# Register your models here.
admin.site.register(Media)
admin.site.register(MediaImage)
admin.site.register(Book)
admin.site.register(Interaction)

