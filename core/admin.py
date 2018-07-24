from django.contrib import admin
from django import forms
from .models import Photo

class PhotoAdminForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = '__all__'


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm
    list_display = ['caption', 'description', 'category', 'location', 'up_votes', 'down_votes', 'view_count', 'photo_url', 'date_last_modified', 'date_added']
    readonly_fields = ['id', 'photo_url', 'date_last_modified', 'date_added']

admin.site.register(Photo, PhotoAdmin)


