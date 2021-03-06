from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# from django.http import JsonResponse
from users.models import Group, User
from users.forms import GroupForm


def group_list(request):
    user = request.GET["user"]
    qs = Group.objects.filter(user_list__auth_user__username=user)

    return qs
    # return JsonResponse(qs)
    # return JsonResponse([post.as_dict() for post in qs], safe=False)


@require_POST
@csrf_exempt
def group_new(request):
    # app 단에서 데이터를 multipart/form-data 형식으로 올려줘야함!!!
    form = GroupForm(request.POST, request.FILES)
    if form.is_valid():
        group = form.save()
        return {'ok': True}
    return {'ok': False, 'errors': form.errors}


@require_POST
@csrf_exempt
def group_edit(request):
    form = GroupForm(request.POST, request.FILES, initial={'name': json['name']})
    if form.is_valid():
        group = form.save()
        return {'ok': True}
    else:
        return {'ok': False, 'errors': form.errors}


urlpatterns = [
    url(r'^$', group_list),
    url(r'^create/$', group_new),
    url(r'^edit/$', group_edit),
]
