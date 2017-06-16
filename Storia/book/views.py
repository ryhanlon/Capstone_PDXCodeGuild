from django.shortcuts import render

# Create your views here.

def home(request):
    """
    landing page template view

    """
    return render(request, 'home.html')

