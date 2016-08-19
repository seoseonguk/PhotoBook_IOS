from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



from .models import Photo, Moment
from .serializers import (
    PhotoSerializer,
    MomentSerializer,
    MomentCreateSerializer)


class PhotoDetailAPIView(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        print (self.kwargs)
        moment_pk = self.kwargs['moment_pk']
        photo_pk = self.kwargs['photo_pk']
        obj = get_object_or_404(Photo, moment__pk = moment_pk, pk=photo_pk)
        return obj





class PhotoListAPIView(generics.ListAPIView):
    authentication_classess = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classess = [permissions.IsAuthenticated,]
    pagenate_by = 10


class MomentCreateAPIView(generics.CreateAPIView):
    serializer_class = MomentCreateSerializer


class MomentListAPIView(generics.ListAPIView):
    authentication_classess = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    queryset = Moment.objects.all()
    serializer_class = MomentSerializer
    permission_classes = [permissions.IsAuthenticated,]
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