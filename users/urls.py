from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^group/$', views.group_list, name='group_list'),
    url(r'^group/create/$', views.group_new, name='group_new'),
]