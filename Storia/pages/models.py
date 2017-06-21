from django.db import models


# def media_upload_handler(instance, filename) -> str:
#     """
#     Handler to provide link to media images
#
#     """
#
#     return f"{instance}/{Media}/{filename}"


class Media(models.Model):
    """
    Stores the media for html pages (web pages, storybook pages, game pages).

    """

    name = models.CharField(max_length=256)
    slug = models.SlugField(editable=False, blank=True)
    location = models.CharField(max_length=50)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    caption = models.CharField(max_length=62, blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)


    class Meta:
        verbose_name_plural = 'media'

    def __str__(self):
        return self.name


class Page(models.Model):
    """
    Set up the web pages.

    """

    name = models.CharField(max_length=256)
    content = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name