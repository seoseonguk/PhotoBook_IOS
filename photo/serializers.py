from rest_framework import serializers, viewsets

from .models import Photo, Memory


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'image',
            # 'memory',
            'taken_at',
            'created_at'
        ]


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer