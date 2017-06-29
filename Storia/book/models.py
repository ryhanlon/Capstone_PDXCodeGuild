from django.db import models
from accounts.models import User
from pages.models import Page
from django.utils.text import slugify


def cover_media_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to book covers.

    """
    name, extention = filename.split('.')
    name = slugify(name)
    filepath = '.'.join([name, extention])

    path = f"{instance.slug}/{filepath}"
    return path


class Book(models.Model):
    """
    Stores the publishing information for the pages: title, author, pubdate,
    copyright, reading level, word count, isbn.

    """

    title = models.CharField(max_length=256)
    slug = models.SlugField(editable=False, blank=True)

    cover = models.ImageField(upload_to=cover_media_upload_handler, default="default_cover.jpg")
    author = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    pub_date = models.CharField(max_length=64, blank=True, null=True)
    copyright = models.CharField(max_length=64, blank=True, null=True)
    isbn = models.CharField(max_length=17, blank=True, null=True)

    reading_level = models.CharField(max_length=32, blank=True, null=True)
    word_count = models.CharField(max_length=5, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    webpage = models.ForeignKey(Page, related_name='books', blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def page_count(self):
        """
        Gets the page count of a book.  Reverse lookup for BookPage.
        """
        pages = len(self.pages.all())
        return pages

    def save(self, *args, **kwargs):
        """
        Slug for urls.  Cover save img.

        """
        self.slug = slugify(self.title)
        # if self.cover is None:
        #     pass
        # Then auto generate this image.

        super().save(*args, **kwargs)


class BookPage(models.Model):
    """
    Template for the story pages.
    """
    book = models.ForeignKey(Book, related_name='pages')
    slug = models.SlugField(editable=False, blank=True)

    name = models.CharField(max_length=245, blank=True, null=True)
    is_title_page = models.BooleanField(default=False)
    page_order = models.PositiveSmallIntegerField(blank=True, null=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Slug for display_page.
        """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


def media_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to media images

    """

    # return f"{instance.page.name}/{filename}"
    return f"{instance.bookpage.book.title}/{instance.bookpage.name}/{filename}"


class Assets(models.Model):
    """
    Stores media for the storybook and game to be used for layout.

    """
    PAGE_TYPE = (
        ('BPG', 'book pages'),
        ('GPG', 'game pages'),
        ('DPG', 'dashboard pages'),
    )

    ASSET_TYPE = (
        ('AUD', 'audio')
        'Vid', 'video'
    )

    visual_artist = models.CharField(max_length=256)
    animator = models.CharField(max_length=256, blank=True, null=True)
    composer = models.CharField(max_length=256, blank=True, null=True)
    locus = models.PositiveSmallIntegerField(default=0)

    type = models.CharField(max_length=3, choices=PAGE_TYPE)
    slug = models.SlugField(editable=False, blank=True)
    bookpage = models.ForeignKey(BookPage, related_name='visuals')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    content_text = models.TextField(max_length=5000)
    file = models.FileField(upload_to=media_upload_handler, default='default_cover.jpg')

    def __str__(self):
        message = f'{self.bookpage.book.title} | {self.bookpage.name} | Pg {self.bookpage.page_order} | {self.slug}'
        return message




