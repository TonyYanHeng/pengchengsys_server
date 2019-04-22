from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import MyUser
import re


def my_login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'login_register/login.html', context)
    elif request.method == 'POST':
        user_name = request.POST['user_name']
        try:
            user = MyUser.objects.get(user_name=user_name)
            password = request.POST['password']
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home/home.html')
            else:
                context["err_info"] = "密码不正确！"
                return render(request, 'login_register/login.html', context)
        except MyUser.DoesNotExist:
            context["err_info"] = "用户名不存在！"
            return render(request, 'login_register/login.html', context)


def my_logout(request):
    logout(request)
    context = {"err_info": "成功退出登录！"}
    return render(request, 'login_register/login.html', context)


def register(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'login_register/register.html', context)
    elif request.method == 'POST':
        user_name = request.POST['user_name']
        try:
            user = MyUser.objects.get(user_name=user_name)
            context["err_info"] = "该用户名已经被注册了！"
            return render(request, 'login_register/register.html', context)
        except MyUser.DoesNotExist:
            phone_num = request.POST['phone_num']
            phone_rule = r'^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$'
            if not re.match(phone_rule, phone_num):
                context["err_info"] = "手机号码输入不正确！"
                return render(request, 'login_register/register.html', context)
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 != password2:
                context["err_info"] = "两次输入的密码不一致！"
                return render(request, 'login_register/register.html', context)
            else:
                user = MyUser.objects.create_user(user_name, phone_num, password1)
                context["err_info"] = "注册成功！"
                return render(request, 'login_register/register.html', context)
