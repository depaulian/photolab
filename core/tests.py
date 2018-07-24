import unittest
from django.urls import reverse
from django.test import Client
from .models import Photo
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_photo(**kwargs):
    defaults = {}
    defaults["caption"] = "caption"
    defaults["description"] = "description"
    defaults["category"] = "category"
    defaults["location"] = "location"
    defaults["up_votes"] = "up_votes"
    defaults["down_votes"] = "down_votes"
    defaults["view_count"] = "view_count"
    defaults["photo_url"] = "photo_url"
    defaults["date_last_modified"] = "date_last_modified"
    defaults.update(**kwargs)
    if "owner" not in defaults:
        defaults["owner"] = create_user()
    return Photo.objects.create(**defaults)


class PhotoViewTest(unittest.TestCase):
    '''
    Tests for Photo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_photo(self):
        url = reverse('core_photo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_photo(self):
        url = reverse('core_photo_create')
        data = {
            "caption": "caption",
            "description": "description",
            "category": "category",
            "location": "location",
            "up_votes": "up_votes",
            "down_votes": "down_votes",
            "view_count": "view_count",
            "photo_url": "photo_url",
            "date_last_modified": "date_last_modified",
            "owner": create_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_photo(self):
        photo = create_photo()
        url = reverse('core_photo_detail', args=[photo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_photo(self):
        photo = create_photo()
        data = {
            "caption": "caption",
            "description": "description",
            "category": "category",
            "location": "location",
            "up_votes": "up_votes",
            "down_votes": "down_votes",
            "view_count": "view_count",
            "photo_url": "photo_url",
            "date_last_modified": "date_last_modified",
            "owner": create_user().pk,
        }
        url = reverse('core_photo_update', args=[photo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


