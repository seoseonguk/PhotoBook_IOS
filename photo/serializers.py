from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework import routers, serializers, viewsets, permissions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Photo, Memory


class PhotoUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    pass


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
