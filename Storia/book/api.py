# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from datetime import datetime
#
# from rest_framework import viewsets
# from .models import Interaction
# from .serializers import InteractionModelSerializer
#
#
# class InteractionViewSet(viewsets.ModelViewSet):
#     """
#     All of the views as an api for CRUD views.
#
#     """
#     model = Interaction
#     queryset = Interaction.objects.all()
#     serializer_class = InteractionModelSerializer
#
#
# @api_view(['POST'])
# def create_interaction(request):
#     """
#     REST end point for creating interaction.
#
#     """
#     value = request.POST['value']
#
#     now = datetime.now()
#     interaction = Interaction(actor=request.user, start=now,
#                               value=value)
#     return Response()