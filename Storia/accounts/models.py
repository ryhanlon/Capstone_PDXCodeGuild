from django.db import models
from django.contrib.auth.models import AbstractUser
# from insights.models import Merit, Awardance


def user_media_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to media images

    """

    # return f"{instance.page.name}/{filename}"
    return f"{instance.image}/{filename}"


class Profile(models.Model):
    """
    Collects the clicks from the story page.  Sent by AJAX call.
    """

    life_clicks = models.PositiveIntegerField(default=1)


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
    merits = models.ManyToManyField('insights.Merit', blank=True)
    profile = models.OneToOneField(Profile, null=True, blank=True)

    REQUIRED_FIELDS = ['nickname', 'email']