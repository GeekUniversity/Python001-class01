# Author Andy Fang
# -*- coding:utf-8 -*-

from django.contrib import admin
from django.urls import path
from . import  views


urlpatterns = [
    path('index.html',views.get_index),
    path('charts.html',views.get_charts),
    path('tables.html',views.get_tables),
    path('content.html',views.get_detail),
]