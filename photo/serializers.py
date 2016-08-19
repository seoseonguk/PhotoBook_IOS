from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework import routers, serializers, viewsets, permissions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Photo, Memory


class PhotoUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        kwargs = {
            'group_pk': obj.memory.group.pk,
            'memory_pk': obj.memory.pk,
            'photo_pk': obj.pk,
        }
        return reverse(view_name, kwargs=kwargs, request=request, format=format)


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    # url = PhotoUrlHyperlinkedIdentityField('photo_list_api')

    class Meta:
        model = Photo
        fields = [
            # 'url',
            'id',
            'image',
            # 'memory',
            'taken_at',
            'created_at',
        ]


class MemoryUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        kwargs = {
            'group_pk': obj.group.pk,
            'moment_pk': obj.pk,
        }
        return reverse(view_name, kwargs=kwargs, request=request, format=format)


class MemorySerializer(serializers.HyperlinkedModelSerializer):
    url = MemoryUrlHyperlinkedIdentityField('api:moment_detail_api')
    # photo_list = serializers.SerializerMethodField(read_only=True)

    # def get_photo_list(self, instance):
    #     queryset = Photo.objects.filter(memory=instance)
    #     serializer = PhotoSerializer(queryset, context={"request":instance}, many=True)
    #     return serializer.data

    class Meta:
        model = Memory
        fields = [
            'url',
            'id',
            'title',
            # 'photo_list',
            'taken_at',
        ]