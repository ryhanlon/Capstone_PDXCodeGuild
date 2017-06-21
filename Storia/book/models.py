from django.db import models
from django.contrib.auth.models import User


class BookMedia(models.Model):
    """
    Stores media for the storybook and game to be used for layout.

    """
    PAGE_TYPE = (
        ('BPG', 'pages pages'),
        ('GPG', 'game pages'),
        ('DPG', 'dashboard pages'),
    )

    visual_artist = models.CharField(max_length=256)
    animator = models.CharField(max_length=256, blank=True, null=True)
    composer = models.CharField(max_length=256, blank=True, null=True)

    type = models.CharField(max_length=3, choices=PAGE_TYPE)
    slug = models.SlugField(editable=False, blank=True)
    location = models.CharField(max_length=50)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    content_text = models.TextField(max_length=5000)
    file = models.FileField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    """
    Stores the publishing information for the pages: title, author, pubdate,
    copyright, reading level, word count, isbn.

    """

    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    pub_date = models.CharField(max_length=64)
    copyright = models.CharField(max_length=64)
    isbn = models.CharField(max_length=17)
    reading_level = models.CharField(max_length=32)
    word_count = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Interaction(models.Model):
    """
    Stores the date captured during the pages interaction: time on the pages,
    words clicked, audio clicked, videos clicked.
    """
    # data from the pages
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