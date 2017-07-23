import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestAssertion:
    """
    Test models.
    """
    def test_truncator(self):
        """
        Testing the truncator.

        """
        asset = mixer.blend('book.Asset', text="Boogie Down")
        result = asset.truncator(amount=6)
        expected = 'Boogie'
        assert result != True, "Has no content."
        assert result == expected, 'Must!! return 6 characters'

        asset2 = mixer.blend('book.Asset', text='Mic Drop!')
        result = asset2.truncator(amount=3)
        expected = 'Mic'
        assert result == expected, 'MUST return 3 charactors, sugarpie'

        asset3 = mixer.blend('book.Asset', text=None)
        result = asset3.truncator(amount=5)
        expected = None
        assert result == expected, 'Must return none if the text is none.'

