from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from .models import Photo

class PhotoListView(ListView):
    model = Photo


class PhotoDetailView(DetailView):
    model = Photo
