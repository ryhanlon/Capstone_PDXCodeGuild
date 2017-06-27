from django.conf.urls import url
from .views import register, login, logout, profile


urlpatterns = [
    url(r'register/', register, name='register'),
    url(r'login/', login, name='login'),
    url(r'logout/', logout, name='logout'),
    url(r'profile/', profile, name='profile'),
    ]





