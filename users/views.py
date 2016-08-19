from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .forms import GroupForm
from .models import Group


def group_list(request):
    qs = Group.objects.all()
    return qs
    # JsonResponse([post.as_dict() for post in qs], safe=False)
    # a = request.user
    # qs = Group.objects.filter(user_list=a.id)

    # return render(request, 'users/group_list.html', {
    #     'group_list': qs,
    # })


def group_new(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('/')
    else:
        form = GroupForm()
    return render(request, 'users/group_form.html', {
        'form': form,
    })


def group_edit(request):
    pass