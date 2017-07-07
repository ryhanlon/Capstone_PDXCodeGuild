import pytest
from django.test import RequestFactory
pytestmark = pytest.mark.django_db

from pages.views import home


class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = home(req)
        assert resp.status_code == 200, 'Must be callable by anyone'