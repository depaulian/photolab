from . import models

from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Photo
        fields = (
            'pk', 
            'caption', 
            'description', 
            'category', 
            'location', 
            'up_votes', 
            'down_votes', 
            'view_count', 
            'photo_url', 
            'date_last_modified', 
            'date_added', 
        )


