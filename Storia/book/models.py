from django.db import models


class BookPage(models.Model):
    """
    Stores the number of pages and format for each page of the story.  (Title page, 1-12 story pages, 'the end' page)
    """
    play_icon =
    stop_icon =
    pause_icon =
    content =


class MediaBookPage(models.Model):
    """
    Stores the media for the each story page (images, video, audio).
    """
    video = models.FileField(upload_to='', null=True)
    audio = models.FileField(upload_to='', null=True)
    image = models.ImageField(upload_to='', null=True)


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


class Interaction(models.Model):
    """
    Stores the date captured during the page interaction: time on the page,
    words clicked, audio clicked, videos clicked.
    """
    # data from the page
    start = models.DateTimeField()
    duration = models.DurationField()
    end = models.DateTimeField()
    word_clicks = models.PositiveSmallIntegerField()
    video_clicks = models.PositiveSmallIntegerField()
    audio_clicks = models.PositiveSmallIntegerField()