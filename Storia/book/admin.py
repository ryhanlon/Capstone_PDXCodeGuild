from django.contrib import admin
from .models import BookMedia, Book, Interaction, BookPage
from django.contrib import admin


class BookPageInline(admin.StackedInline):
    model = BookPage


class BookAdmin(admin.ModelAdmin):
    inlines = [
        BookPageInline,

    ]

admin.site.register(BookMedia)
admin.site.register(Book, BookAdmin)
admin.site.register(Interaction)

