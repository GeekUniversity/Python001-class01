# Author Andy Fang
# -*- coding:utf-8 -*-
from django.contrib import admin
from django.urls import path
from  . import views
urlpatterns = [
    path('index',views.get_index),
    path('error', views.get_error),
    path('login2',views.login2),
]
