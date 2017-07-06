import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from accounts.views import profile


class TestAdminView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = profile(req)
        assert 'login' in resp.url, 'Must redirect to login'

    def test_superuser(self):
        user = mixer.blend('accounts.User', is_superuser=True)
        req = RequestFactory().get('/')
        req.user = user
        resp = profile(req)
        assert resp.status_code == 200, 'Must be callable by superuser'
