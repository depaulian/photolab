from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Photo(models.Model):
    PEOPLE = 'PEOPLE'
    NATURE = 'NATURE'
    CITY_LIFE = 'CITY_LIFE'
    LOVE = 'LOVE'
    SPORTS = 'SPORTS'
    FAMILY = 'FAMILY'
    GENERAL = 'General'

    CATEGORY_CHOICES = (
        (PEOPLE, 'People'),
        (NATURE, 'Nature'),
        (CITY_LIFE, 'City Life'),
        (LOVE, 'Love'),
        (SPORTS, 'Sports'),
        (FAMILY, 'Family'),
        (GENERAL, 'General'),
    )
    # Fields
    caption = CharField(max_length=30)
    description = TextField(blank=True)
    category = CharField(max_length=12, choices=CATEGORY_CHOICES, default=GENERAL)
    location = TextField(blank=True)
    up_votes = IntegerField(default=0)
    down_votes = IntegerField(default=0)
    view_count = IntegerField(default=0)
    photo_url = ImageField(upload_to='photos/%Y/%m/%d/%H/%M/%S')
    date_last_modified = DateTimeField(auto_now=True)
    date_added = DateTimeField(auto_now_add=True)

    # Relationship Fields
    owner = ForeignKey(
        User, on_delete=models.PROTECT, related_name='+'
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.caption

    def get_absolute_url(self):
        return reverse('core_photo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('core_photo_update', args=(self.pk,))


