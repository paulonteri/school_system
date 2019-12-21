from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='academics_home'),
    url(r'^search/$', views.exam_performance_search, name='exam_performance_search'),
]