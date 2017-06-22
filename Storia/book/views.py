from django.shortcuts import render
from .models import Book

# from .models import Media, BookMedia
#
#
# def home(request):
#     """
#     landing pages template view, slider/carousel
#
#     """
#
#     slider_images = Media.objects.filter(location='carousel')
#
#     context = {'slider_images': slider_images}
#
#     return render(request, 'home.html', context)
#


def display_book(request, slug):
    """
    To display a book.

    """

    book = Book.objects.get(slug=slug)
    context = {'book': book}
    return render(request, 'book/display_book.html', context)


def bookshelf(request):
    """
    Choose which storybook one wants to read.

    """

    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/bookshelf.html', context)
