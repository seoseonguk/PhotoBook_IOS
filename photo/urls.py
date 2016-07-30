from django.conf.urls import url

from .views import PhotoListView, PhotoDetailView


urlpatterns = [

    url(r'^$', PhotoListView.as_view(), name='photo_list'),
    url(r'^(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo_detail'),


]