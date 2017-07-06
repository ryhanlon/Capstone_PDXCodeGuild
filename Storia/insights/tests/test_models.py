import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestMerit:

    def test_create_merit(self):
        """

        :return:
        """
        merit = mixer.blend('insights.Merit', title='test merit')
        assert merit.pk == 1, "Need to save an instance."
        assert merit.image != None, 'Merit must have an image'
        assert merit.title == 'test merit', "Merit must have a title"

