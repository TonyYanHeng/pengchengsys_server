from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.
def login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'login_register/login.html', context)
    elif request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login_register/home.html')
        else:
            context["err_info"] = "用户名和密码不正确！"
            return render(request, 'login_register/login.html', context)


def register(request):
    return render(request, 'login_register/register.html')
