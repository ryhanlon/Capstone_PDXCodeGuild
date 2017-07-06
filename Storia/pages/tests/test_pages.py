from django.test import RequestFactory

from pages.views import home


class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = home(req)
        assert resp.status_code == 200, 'Must be callable by anyone'