from rest_framework import viewsets
from .models import Interaction
from .serializers import InteractionModelSerializer


class InteractionViewSet(viewsets.ModelViewSet):
    """
    All of the views as an api for CRUD views.

    """
    model = Interaction
    queryset = Interaction.objects.all()
    serializer_class = InteractionModelSerializer