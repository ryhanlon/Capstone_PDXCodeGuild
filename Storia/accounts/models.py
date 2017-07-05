from django.db import models
from django.contrib.auth.models import AbstractUser


def user_media_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to media images

    """

    # return f"{instance.page.name}/{filename}"
    return f"{instance.image}/{filename}"


class User(AbstractUser):
    """

    Users within Django authentication system are
    represented by this model.
    The best users.  They love reading stories.
    Username, password and email are required.

    """

    nickname = models.CharField(max_length=300)
    image = models.ImageField(default='Bunny-avatar.gif', upload_to=user_media_upload_handler)

    REQUIRED_FIELDS = ['nickname', 'email']