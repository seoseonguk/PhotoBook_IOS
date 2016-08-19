from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



from .models import Photo
from .serializers import PhotoSerializer


class PhotoListAPIView(generics.ListAPIView):
    authentication_classess = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classess = [permissions.IsAuthenticated,]
    pagenate_by = 10



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