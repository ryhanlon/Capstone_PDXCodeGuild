from django.db import models
from django.contrib.auth.models import User

# class BookPage(models.Model):
#     """
#     Stores the number of pages and format for each page of the story.  (Title page, 1-12 story pages, 'the end' page)
#     """
#     play_icon =
#     stop_icon =
#     pause_icon =
#     content =


class Media(models.Model):
    """
    Stores the media for html pages (web pages, storybook pages, game pages).

    """
    PAGE_TYPE = (
        ('BPG', 'book page'),
        ('WPG', 'web page'),
        ('GPG', 'game page'),
    )

    name = models.CharField(max_length=256)
    slug = models.SlugField(editable=False, blank=True)
    location = models.CharField(max_length=50)
    caption = models.CharField(max_length=62, blank=True, null=True)
    type = models.CharField(max_length=3, choices=PAGE_TYPE)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    file = models.FileField(blank=True, null=True)  # TODO: upload to

    class Meta:
        verbose_name_plural = 'media'

    def __str__(self):
        return self.name


class MediaImage(Media):
    """
    Stores the media for each story page (images, video, audio).
    """

    image = models.ImageField(blank=True, null=True)     # TODO: upload to
    alt_text = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Stores the publishing information for the book: title, author, pubdate,
    copyright, reading level, word count, isbn.
    """

    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    pub_date = models.CharField(max_length=64)
    copyright = models.CharField(max_length=64)
    reading_level = models.CharField(max_length=32)
    word_count = models.CharField(max_length=32)
    isbn = models.CharField(max_length=17)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Interaction(models.Model):
    """
    Stores the date captured during the page interaction: time on the page,
    words clicked, audio clicked, videos clicked.
    """
    # data from the page
    INTERACTION_TYPE = (
        ('WDC', 'word clicks'),
        ('VDC', 'video clicks'),
        ('ADC', 'audio clicks'),
    )

    start = models.DateTimeField()
    duration = models.DurationField()
    end = models.DateTimeField()
    type = models.CharField(max_length=3, choices=INTERACTION_TYPE)
    actor = models.ForeignKey(User, related_name='interactions')

    def __str__(self):
        return self.type