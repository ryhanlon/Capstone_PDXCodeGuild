from django.contrib import admin
from .models import BookMedia, Book, Interaction

# Register your models here.

admin.site.register(BookMedia)
admin.site.register(Book)
admin.site.register(Interaction)

