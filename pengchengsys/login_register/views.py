from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'login_register/login.html')


def register(request):
    return render(request, 'login_register/register.html')
