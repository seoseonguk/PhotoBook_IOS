from django.conf.urls import url, include


from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token




urlpatterns = [
    url(r'^api/$', 'photobook.views.api_home', name='api_home'),
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/$', obtain_jwt_token),
]
