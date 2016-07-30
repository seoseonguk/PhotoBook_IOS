from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Photo

class PhotoListView(ListView):
    model = Photo


class PhotoDetailView(DetailView):
    model = Photo


class PhotoCreateView(CreateView):
    model = Photo
    fields = '__all__'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = '__all__'


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:photo_list')