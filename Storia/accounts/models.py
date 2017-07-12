from django.db import models
from django.contrib.auth.models import AbstractUser
# from insights.models import Merit, Awardance


def user_media_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to media images

    """

    # return f"{instance.page.name}/{filename}"
    return f"{instance.title}/{filename}"


class Profile(models.Model):
    """
    Collects the clicks from the story page.  Sent by AJAX call.
    """

    life_clicks = models.PositiveIntegerField(default=1)


class Merit(models.Model):
    """
    Manages the merits that each user can earn.

    """
    image = models.ImageField(upload_to=user_media_upload_handler)
    stage = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=256)

    def __str__(self):
        return f"Level and types of awards to earn."


class User(AbstractUser):
    """

    Users within Django authentication system are
    represented by this model.
    The best users.  They love reading stories.
    Username, password and email are required.
    ManyToMany relationship between User | Merit, through table Awardance.

    """

    nickname = models.CharField(max_length=300)
    image = models.ImageField(default='Bunny-avatar.gif', upload_to=user_media_upload_handler)
    merits = models.ManyToManyField(Merit, blank=True, through='Awardance', related_name='users')
    profile = models.OneToOneField(Profile, null=True, blank=True)

    REQUIRED_FIELDS = ['nickname', 'email']


class Awardance(models.Model):
    """
    Through table for ManyToMany relation.
    User 'awards' | Merit 'recognitions
    """
    user = models.ForeignKey(User, related_name='awards')
    merit = models.ForeignKey(Merit, related_name='recognitions')

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History of {self.user.username}'s awards."

