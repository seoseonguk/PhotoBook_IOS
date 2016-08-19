from django.conf.urls import url, include


from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from photo.views import PhotoListAPIView


urlpatterns = [

    url(r'^photolist/$', PhotoListAPIView.as_view(), name='photo_list_api'),

    # url(r'^$', 'photobook.views.api_home', name='api_home'),

    # # 유저의 그룹을 요청하는 리스트 ( USER 가 자신이 속한 Group의 리스트를 받을 수 있는 뷰 )
    # url(r'^group/$', ),
    # # 특정 그룹을 생성하는 API ( 그룹 이름, 전화번호 하나를 넘겼을 때 받아서, 문자 PUSH 하는 기능이 있어야 함! )
    # url(r'^group/create/$', ),
    # # 특정 그룹을 편집하는 API ( 그룹 이름, 메인 사진 바꾸는 것 )
    # url(r'^group/(?P<group_pk>\d+)/edit/$', ),


    # # 전체 사진 리스트 호출 API ( 일자별로 사진을 묶어서 보내줘야한다. )
    # url(r'^group/(?P<group_pk>\d+)/$', name='photo_list_api'),


    # # 사진 생성 url
    # url(r'^group/(?P<group_pk>\d+)/image/create/$', ),
    # # 사진 좋아요 url
    # url(r'^group/(?P<group_pk>\d+/image/(?P<moment_pk\d+)/like/$)'),
    # # 사진 삭제 url
    # url(r'^group/(?P<group_pk>\d+/image/(?P<moment_pk\d+)/delete/$)'),


    # 사진
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/$', obtain_jwt_token),
]
