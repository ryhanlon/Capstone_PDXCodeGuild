from django.contrib import admin
from .models import Asset, Book, BookPage
from django.contrib import admin


class BookPageInline(admin.StackedInline):
    model = BookPage


class BookAdmin(admin.ModelAdmin):
    inlines = [
        BookPageInline,
    ]


class AssetPageInLine(admin.StackedInline):
    model = Asset


class BookPageAdmin(admin.ModelAdmin):
    inlines = [
        AssetPageInLine
    ]


admin.site.register(BookPage, BookPageAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Asset)


