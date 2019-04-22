#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path
from . import views


app_name = 'login_register'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
