from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^group/$', views.group_list, name='group_list'),
    url(r'^group/create/$', views.group_new, name='group_new'),
    url(r'^api/v1/', include('users.api.v1')),
]