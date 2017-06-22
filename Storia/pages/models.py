from django.db import models


def media_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to media images

    """

    return f"{instance.page.name}/{filename}"


class Page(models.Model):
    """
    Identifies the web page.  Text field for the main text for the page(optional).

    """

    name = models.CharField(max_length=256)
    slug = models.SlugField(editable=False, blank=True)
    content = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Media(models.Model):
    """
    Stores the media for each web page (html, website centered).

    """

    page = models.ForeignKey(Page, related_name='contents')
    name = models.CharField(max_length=256)
    slug = models.SlugField(editable=False, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    caption = models.CharField(max_length=62, blank=True, null=True)
    file = models.FileField(upload_to=media_upload_handler, blank=True, null=True)
    image = models.ImageField(upload_to=media_upload_handler, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'media'

    def __str__(self):
        return self.name


