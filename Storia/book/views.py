from django.shortcuts import render
from .models import Media, MediaImage


def home(request):
    """
    landing page template view

    """

    slider_images = Media.objects.filter(location='carousel')

    context = {'slider_images': slider_images}

    return render(request, 'home.html', context)


def contact(request):
    """
    landing page template view

    """
    return render(request, 'contact.html')


def about(request):
    """
    landing page template view

    """
    return render(request, 'about.html')



