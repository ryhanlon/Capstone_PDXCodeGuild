from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from rest_framework import viewsets
from .models import Interaction, AssetInteraction
from .serializers import InteractionModelSerializer



class InteractionViewSet(viewsets.ModelViewSet):
    """
    All of the views as an api for CRUD views.

    """
    model = Interaction
    queryset = Interaction.objects.all()
    serializer_class = InteractionModelSerializer

