from rest_framework import viewsets

from . import serializers as emails_serializers
from .serializers import email_models


class EmailModelViewSet(viewsets.ModelViewSet):
    serializer_class = emails_serializers.EmailSerializer
    queryset = email_models.Email.objects.all()
