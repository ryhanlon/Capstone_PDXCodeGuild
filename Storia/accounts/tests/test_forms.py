import pytest
from accounts.forms import CustomUserUpdateForm
pytestmark = pytest.mark.django_db


# class TestUserUpdateForm:
#     """
#     Test and build the Update Account Form.
#     """
#     def test_form(self):
#         form = CustomUserUpdateForm(data={})
#         assert form.is_valid() is False, 'Must be invalid if no data is given'
#
#     data = {'username': '1234'}
#     form = CustomUserUpdateForm(data=data)
#     assert form.is_valid() is False, 'Name must be letters, not digits'
#     assert 'username' in form.errors, 'Must return field error for username'
#
#     data = {'username': 'Joanna'}
#     form = CustomUserUpdateForm(data=data)
#     assert form.is_valid() is True, 'Must be valid when data is given'