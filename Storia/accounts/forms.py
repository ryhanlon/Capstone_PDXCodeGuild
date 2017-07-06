from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """


    """
    nickname = forms.RegexField(label=('Nickname'), max_length=300,
                                regex=r'^[\w.@+\s]+$')
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('nickname', 'email', 'image', )


# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta(UserChangeForm):
#         model = User
#         fields = UserChangeForm.Meta.fields + 'nickname'


class CustomUserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'nickname', 'first_name', 'last_name', )