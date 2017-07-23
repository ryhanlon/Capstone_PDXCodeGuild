from django.shortcuts import render
from .models import Book, BookPage


def story_page(request, book_slug, page_slug):
    """
    Directing layout assets to story_page.html (storybook page).
    """

    page = BookPage.objects.get(book__slug=book_slug, slug=page_slug)

    assets = page.assets.all()
    lines = page.lines.all()
    merits = request.user.merits.order_by('-stage')

    asset_data = {
              'video': assets.filter(type='VID')[0],
              'record_icon': assets.filter(type='IMA'),
              'lines': lines,
              'merits': merits,
             }

    context = {'page': page, 'assets': asset_data}
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



