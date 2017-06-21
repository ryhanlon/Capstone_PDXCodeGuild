from django.shortcuts import render
from .models import Page, Media


def home(request):
    """
    Landing pages template view, slider/carousel.

    """

    slider_images = Media.objects.filter(location='carousel')

    context = {'slider_images': slider_images}

    return render(request, 'home.html', context)


def contact(request):
    """
    Landing pages template view.

    """
    return render(request, 'contact.html')


def about(request):
    """
    Landing pages template view.

    """
    return render(request, 'about.html')