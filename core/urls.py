from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'photo', api.PhotoViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Photo
    path('core/photo/', views.PhotoListView.as_view(), name='core_photo_list'),
    path('core/photo/create/', views.PhotoCreateView.as_view(), name='core_photo_create'),
    path('core/photo/detail/<int:pk>/', views.PhotoDetailView.as_view(), name='core_photo_detail'),
    path('core/photo/update/<int:pk>/', views.PhotoUpdateView.as_view(), name='core_photo_update'),
)

