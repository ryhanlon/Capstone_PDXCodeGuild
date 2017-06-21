from django.shortcuts import render
# from .models import Media, BookMedia
#
#
# def home(request):
#     """
#     landing pages template view, slider/carousel
#
#     """
#
#     slider_images = Media.objects.filter(location='carousel')
#
#     context = {'slider_images': slider_images}
#
#     return render(request, 'home.html', context)
#
#
# def contact(request):
#     """
#     landing pages template view
#
#     """
#     return render(request, 'contact.html')
#
#
# def about(request):
#     """
#     landing pages template view
#
#     """
#     return render(request, 'about.html')
