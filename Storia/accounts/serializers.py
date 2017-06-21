from rest_framework import serializers
from .models import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
     All of the views as an api for CRUD views.

    """
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
