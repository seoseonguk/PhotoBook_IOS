from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework import routers, serializers, viewsets, permissions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Photo, Moment



class PhotoUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        kwargs = {
            'group_pk': obj.moment.group.pk,
            'moment_pk': obj.moment.pk,
            'photo_pk': obj.pk,
        }
        return reverse(view_name, kwargs=kwargs, request=request, format=format)


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    url = PhotoUrlHyperlinkedIdentityField('api:photo_detail_api')

    class Meta:
        model = Photo
        fields = [
            'url',
            'id',
            'image',
            'taken_at',
            'created_at',
        ]


class MomentUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        kwargs = {
            'group_pk': obj.group.pk,
            'moment_pk': obj.pk,
        }
        return reverse(view_name, kwargs=kwargs, request=request, format=format)


# class MomentCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Moment
#         fields = [
#             '',
#             '',
#             '',
#         ]


class MomentSerializer(serializers.HyperlinkedModelSerializer):
    url = MomentUrlHyperlinkedIdentityField('api:moment_detail_api')
    photo_set = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Moment
        fields = [
            'url',
            'id',
            'title',
            'photo_set',
            'taken_at',
        ]