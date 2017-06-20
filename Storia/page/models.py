from django.db import models

# Create your models here.

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
    caption = models.CharField(max_length=62, blank=True, null=True)

    created = models.DateTimeField()
    modified = models.DateTimeField()
    file = models.FileField(blank=True, null=True)
    image = models.ImageField(blank =True, null=True)

    class Meta:
        verbose_name_plural = 'media'

    def __str__(self):
        return self.name


class Page(models.Model):
    """
    Set up the web page.

    """

    WEB_PG_TYPE = (
        ('HPG', 'home page'),
        ('APG', 'about page'),
        ('CPG', 'contact page'),
    )

    web_page = models.CharField(max_length=3, choices=WEB_PG_TYPE)