from django.shortcuts import render
from .models import Media, MediaImage


def home(request):
    """
    landing page template view

    """

    slider_images = Media.objects.filter()



    return render(request, 'home.html')


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



