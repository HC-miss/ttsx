from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        print(username, pwd, cpwd, email, allow)
        filter_result = User.objects.filter(username=username)
        if filter_result:
            messge = '当前用户名已存在'
            return render(request, 'register.html', {'messge ': messge })
        return HttpResponse('ok')

    else:
        return render(request, 'register.html')


def login(request):
    return None