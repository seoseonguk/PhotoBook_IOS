from datetime import datetime

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



from .models import Photo, Moment
from .serializers import (
    PhotoSerializer,
    PhotoCreateSerializer,
    PhotoLikedSerializer,
    MomentSerializer,
    MomentCreateSerializer)


from users.models import Group

class PhotoLikedAPIView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoLikedSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        print (self.kwargs)
        moment_pk = self.kwargs['moment_pk']
        photo_pk = self.kwargs['photo_pk']
        obj = get_object_or_404(Photo, moment__pk = moment_pk, pk=photo_pk)
        return obj

    def put(self, request, *args, **kwargs):
        print (self)
        return self.update(request, *args, **kwargs)


class PhotoDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        print (self.request.META)
        moment_pk = self.kwargs['moment_pk']
        photo_pk = self.kwargs['photo_pk']
        obj = get_object_or_404(Photo, moment__pk = moment_pk, pk=photo_pk)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PhotoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoCreateSerializer

    def create(self, request, *args, **kwargs):
        print (request.data)
        taken_at = request.data['taken_at']
        print(taken_at)
        date = datetime.strptime(taken_at, "%Y-%m-%dT%H:%M").date()
        print (date)
        group = get_object_or_404(Group, pk=kwargs['group_pk'])
        moment = Moment.objects.get_or_create(group=group, taken_at=date)[0]
        print (moment)
        photo = Photo.objects.create(
                owner=request.user.user_model,
                image=request.data['image'],
                moment=moment,
                taken_at=taken_at,
            )
        # photo_serializer = PhotoSerializer(data=photo)
        # photo_serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_201_CREATED)


class PhotoListAPIView(generics.ListAPIView):
    authentication_classess = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classess = [permissions.IsAuthenticated,]
    pagenate_by = 10

    def get_queryset(self, *args, **kwargs):
        print()
        obj_list = Photo.objects.filter(moment__pk=self.kwargs['moment_pk'])
        return obj_list

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