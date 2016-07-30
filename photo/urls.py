from django.conf.urls import url

from .views import PhotoListView, PhotoDetailView, PhotoUpdateView, PhotoCreateView, PhotoDeleteView


urlpatterns = [

    url(r'^$', PhotoListView.as_view(), name='photo_list'),
    url(r'^create/$', PhotoCreateView.as_view(), name='photo_create'),
    url(r'^(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo_detail'),
    url(r'^(?P<pk>\d+)/update/$', PhotoUpdateView.as_view(), name='photo_update'),
    url(r'^(?P<pk>\d+)/delete/$', PhotoDeleteView.as_view(), name='photo_delete'),

]

