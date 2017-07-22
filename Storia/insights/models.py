from django.db import models
from book.models import Asset, BookPage, Word
# from accounts.models import User
from django.utils.text import slugify


class Interaction(models.Model):
    """
    Base model for identifying the user and book for interaction tracking.
    ForeignKey: with User 'interactions'
    """

    slug = models.SlugField(editable=False, blank=True)
    user = models.ForeignKey('accounts.User', related_name='interactions')

    def __str__(self):
        return f"{self.user.username}'s interactions."

    def save(self, *args, **kwargs):
        """
        Slug for urls.

        """
        self.slug = slugify(self.user)

        super().save(*args, **kwargs)


class AssetInteraction(Interaction):
    """
    Keep track of clicks on audio, video and words.
    ForeignKey: with Asset | 'clicks'

    """
    INTERACTION_TYPE = (
        ('WDC', 'word clicks'),
        ('VDC', 'video clicks'),
        ('ADC', 'audio clicks'),
    )

    asset = models.ForeignKey(Asset, related_name='clicks')

    type = models.CharField(max_length=3, choices=INTERACTION_TYPE)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s {self.value} clicks on {self.asset}."


class TimeInteraction(Interaction):
    """
    The time spent on each story_page or game_page.
    ForeignKey: with BookPage | 'dwell_times'

    """

    PAGE_TYPE = (
        ('SPG', 'story page'),
        ('GPG', 'game page'),
    )

    page = models.ForeignKey(BookPage, related_name='dwell_times')
    page_type = models.CharField(max_length=3, choices=PAGE_TYPE)
    start = models.DateTimeField()
    duration = models.DurationField(blank=True, null=True)
    end = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username}'s {self.duration} time on story/game page."

    def calculate_duration(self):
        """
        Calculate duration.
        """
        self.duration = self.end - self.start
        return self.duration


