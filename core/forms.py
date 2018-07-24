from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['caption', 'description', 'category', 'location', 'up_votes', 'down_votes', 'view_count', 'photo_url', 'owner']


