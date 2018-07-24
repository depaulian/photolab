from . import models
from . import serializers
from rest_framework import viewsets, permissions


class PhotoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Photo class"""

    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]


