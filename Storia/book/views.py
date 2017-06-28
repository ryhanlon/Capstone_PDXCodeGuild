from django.shortcuts import render
from .models import Book, BookPage

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


def story_page(request, book_slug, page_slug):
    """

    """

    page = BookPage.objects.get(book__slug=book_slug, slug=page_slug)
    assets = {p.locus: p for p in page.visuals.order_by('locus')}

    context = {'page': page, 'assets': assets}
    return render(request, "book/story_page.html", context)


def display_book(request, slug):
    """
    To display a book.

    """

    book = Book.objects.get(slug=slug)
    pages = book.pages.filter(is_title_page=False).order_by('page_order')
    title_page = book.pages.get(is_title_page=True)

    context = {'book': book, 'pages': pages, 'title_page': title_page}
    return render(request, 'book/display_book.html', context)


def bookshelf(request):
    """
    Choose which storybook one wants to read.

    """

    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/bookshelf.html', context)



