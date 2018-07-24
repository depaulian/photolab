from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Photo
from .forms import PhotoForm


class PhotoListView(ListView):
    model = Photo


class PhotoCreateView(CreateView):
    model = Photo
    form_class = PhotoForm


class PhotoDetailView(DetailView):
    model = Photo


class PhotoUpdateView(UpdateView):
    model = Photo
    form_class = PhotoForm

