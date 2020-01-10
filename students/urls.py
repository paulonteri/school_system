from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='students_home'),
    url(r'^search/$', views.student_search, name='student_list_search'),
    url('add_student', views.add_student_view, name='add_student'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name="student_detail"),
]
