from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework import routers, serializers, viewsets, permissions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Photo, Memory




# class PhotoSerializer(serailizers.HyperlinkedModelSerializer):
#     url =



# class PhotoSerializer(serializers.HyperlinkedModelSerializer):
#     memory_title = serializers.CharField(source='memory.title', read_only=True)
#     class Meta:
#         model = Photo
#         fields = [
#             'image',
#             'memory_title',
#             'taken_at',
#             'created_at'
#         ]


# class PhotoViewSet(viewsets.ModelViewSet):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer


# class MemorySerailizer(serializers.HyperlinkedModelSerializer):
#     photo_set = PhotoSerializer(many=True, read_only=True)
#     class Meta:
#         model = Memory
#         fields = [
#             'title',
#             'image',
#             'taken_at',
#             'created_at',
#             'photo_set'
#         ]


# class MemoryViewSet(viewsets.ModelViewSet):
#     queryset = Memory.objects.all()
#     serializer_class = MemorySerailizer

