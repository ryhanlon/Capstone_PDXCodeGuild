"""Storia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from pages.views import  home, about, contact
from book.views import display_book, bookshelf, story_page

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from accounts.api import UserViewSet
from insights.api import InteractionViewSet, create_interaction

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'interactions', InteractionViewSet)


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),

    # Accounts
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Books
    url(r'^books/bookshelf', bookshelf, name='bookshelf'),
    url(r'^books/(?P<slug>[a-z0-9\-]+)$', display_book, name='display_book'),
    url(r'^books/(?P<book_slug>[a-z0-9\-]+)/(?P<page_slug>[a-z0-9\-]+)', story_page, name='story_page'),

    # Insights
    url(r'^insights/clicks', create_interaction, name='create_interaction'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

