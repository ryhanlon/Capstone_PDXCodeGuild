from django.db import models
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
    ForeignKey: pages.Page 'books'

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
    webpage = models.ForeignKey('pages.Page', related_name='books', blank=True, null=True)

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

        super().save(*args, **kwargs)


class BookPage(models.Model):
    """
    Template for the story pages.
    ForeignKey: with Book 'pages'
    """
    PAGE_TYPE = (
        ('BPG', 'book pages'),
        ('GPG', 'game pages'),
        ('DPG', 'dashboard pages'),
    )

    book = models.ForeignKey(Book, related_name='pages')
    slug = models.SlugField(editable=False, blank=True)
    type = models.CharField(max_length=3, choices=PAGE_TYPE)

    name = models.CharField(max_length=245, blank=True, null=True)
    is_title_page = models.BooleanField(default=False)
    page_order = models.PositiveSmallIntegerField(blank=True, null=True)
    headline = models.TextField()
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


def book_media_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to media images

    """

    return f"{instance.bookpage.book.title}/{instance.bookpage.name}/{filename}"


class Line(models.Model):
    """
    Assign each TXA type (text and audio) to a text line on the page.
    Foreign key with Page 'lines'
    """
    order = models.PositiveSmallIntegerField()
    page = models.ForeignKey(BookPage, related_name="lines")
    audio = models.FileField(upload_to=book_media_upload_handler)

    def __str__(self):
        message = f'{self.order} | {self.bookpage.book.title}'

        return message


class Asset(models.Model):
    """
    Stores media for the storybook and game to be used for layout.
    Foreign Key: with BookPage 'assets'

    """
    ASSET_TYPE = (
        ('AUD', 'audio'),
        ('VID', 'video'),
        ('IMG', 'image'),
        ('IMA', 'image and audio'),
        ('TXA', 'text and audio'),
    )

    visual_artist = models.CharField(max_length=256)
    animator = models.CharField(max_length=256, blank=True, null=True)
    composer = models.CharField(max_length=256, blank=True, null=True)
    locus = models.PositiveSmallIntegerField(default=0)

    slug = models.SlugField(editable=False, blank=True)
    bookpage = models.ForeignKey(BookPage, related_name='assets')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    type = models.CharField(max_length=3, choices=ASSET_TYPE)
    file = models.FileField(upload_to=book_media_upload_handler, blank=True, null=True)

    def truncator(self, amount=25):
        """
        Truncates text, shorten for the __str__
        """
        if self.text is not None:

            text = self.text[:amount]
            return text

        else:
            return None

    def __str__(self):

        message = f'{self.bookpage.book.title} | {self.bookpage.name} | ' \
                  f'Pg {self.bookpage.page_order} | {self.type} | {self.truncator()} | {self.slug}'

        return message


class Word(Asset):
    """
    Combining the word and audio file, word count.
    Foreign Key: with Line 'words'
    """
    text = models.CharField(max_length=256, blank=True, null=True)
    audio = models.FileField(upload_to=book_media_upload_handler, blank=True, null=True)
    length = models.PositiveSmallIntegerField()
    line = models.ForeignKey(Line, related_name="words")

    def __len__(self):
        """
        Counts the letters of each word.
        """
        return len(self.word)

    def __add__(self, other):
        """
        Allows to concat with +
        """
        return self.word + other.word

    def __str__(self):
        message = f'{self.word} | {self.bookpage.book.title}'

        return message

