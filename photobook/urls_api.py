from django.conf.urls import url, include


from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from photo.views import PhotoListAPIView, MomentListAPIView, PhotoDetailAPIView, PhotoCreateAPIView, MomentCreateAPIView


urlpatterns = [

    # '''
    # # 전체 ROOT API HOME
    # url(r'^$', 'photobook.views.api_home', name='api_home'),

    # ----- 그룹 생성 관련 기능 -----
    # # 회원 가입 관련 기능
    # 기본 가입 API
    # 소셜 가입 API


    # ----- 그룹 관련 기능 -----
    # # 유저의 그룹을 요청하는 리스트
    # ( USER 가 자신이 속한 Group의 리스트를 받을 수 있는 뷰
    #   유저 정보를 받아서, 유저가 키로 가지고 있는 Group의 리스트를 받을 수 있음 )
    # url(r'^group/$',,name='group_list_api'),
    # # 특정 그룹을 생성하는 API
    # ( 그룹 이름, 전화번호 하나를 넘겼을 때 받아서, 문자 PUSH 하는 기능이 있어야 함! )
    # url(r'^group/create/$',,name='group_create_api'),
    # # 특정 그룹을 편집하는 API ( 그룹 이름, 메인 사진 바꾸는 것 )
    # url(r'^group/(?P<group_pk>\d+)/edit/$',,name='group_edit_api'),


    # ----- 모멘트 관련 기능 ----
    # 전체 사진 리스트뷰 로드 API
    url(r'^group/(?P<group_pk>\d+)/moment/$', MomentListAPIView.as_view(), name='moment_list_api'),
    url(r'^group/(?P<group_pk>\d+)/moment/(?P<moment_pk>\d+)/$', PhotoListAPIView.as_view(), name='moment_detail_api'),
    # Moment 도 생성(뺄려고 했는데, 필요할 것 같아요)
    url(r'^group/(?P<group_pk>\d+/moment/create/$)', MomentCreateAPIView.as_view(), name='moment_create_api'),

    # 사진 개별 detail view
    url(r'^group/(?P<group_pk>\d+)/moment/(?P<moment_pk>\d+)/(?P<photo_pk>\d+)/$', PhotoDetailAPIView.as_view(), name='photo_detail_api'),
    # '''
    # # 사진 생성 url
    url(r'^group/(?P<group_pk>\d+)/moment/(?P<moment_pk>\d+)/create/$', PhotoCreateAPIView.as_view(), name='photo_create_api'),
    # # 사진 좋아요 url
    # url(r'^group/(?P<group_pk>\d+/moment/(?P<moment_pk>\d+)/(?P<photo_pk>\d+)/like/$)'),
    # # 사진 삭제 url
    # url(r'^group/(?P<group_pk>\d+/moment/(?P<moment_pk>\d+)/(?P<photo_pk>\d+)/delete/$)'),
    # '''

    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/$', obtain_jwt_token),
]
