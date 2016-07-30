from django.conf.urls import url, include


from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token


from photo.serializers import PhotoViewSet, MemoryViewSet

router = routers.DefaultRouter()

router.register(r"photos", PhotoViewSet)
router.register(r"memories", MemoryViewSet)


urlpatterns = [
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/$', obtain_jwt_token),
    url(r'^', include(router.urls)),
]
