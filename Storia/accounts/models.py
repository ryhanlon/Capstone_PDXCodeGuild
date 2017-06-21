from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """

    Users within Django authentication system are
    represented by this model.
    The best users.  They love reading stories.
    Username, password and email are required.

    """

    nickname = models.CharField(max_length=300)

    REQUIRED_FIELDS = ['nickname', 'email']