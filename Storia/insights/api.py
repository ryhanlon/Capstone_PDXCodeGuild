from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from rest_framework import viewsets
from .models import Interaction
from .serializers import InteractionModelSerializer
from book.models import Asset
from .models import AssetInteraction


class InteractionViewSet(viewsets.ModelViewSet):
    """
    All of the views as an api for CRUD views.

    """
    model = Interaction
    queryset = Interaction.objects.all()
    serializer_class = InteractionModelSerializer



@api_view(['POST'])
def create_interaction(request):
    """
    REST end point for creating interaction.

    """
    asset_id = request.POST['asset_id']
    asset_type = request.POST['asset_type']

    asset = Asset.objects.get(id=asset_id)

    asset_interaction = AssetInteraction(asset=asset, user=request.user, value=1, type=asset_type)

    asset_interaction.save()

    return Response({'status': "LLAMAS"}, status=status.HTTP_200_OK)