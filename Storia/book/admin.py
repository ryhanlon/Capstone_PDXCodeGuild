from django.contrib import admin
from .models import MediaBookPage, Book, Interaction

# Register your models here.
admin.site.register(MediaBookPage)
admin.site.register(Book)
admin.site.register(Interaction)