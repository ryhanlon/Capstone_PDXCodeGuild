from rest_framework import serializers
from .models import Interaction


class InteractionModelSerializer(serializers.ModelSerializer):
    """
     All of the views as an api for CRUD views.

    """
    class Meta:
        model = Interaction
        fields = ('start', 'duration', 'end', 'type', 'actor')
