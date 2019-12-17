from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('school/', include('school.urls')),
    path('admin/', admin.site.urls),
    path('staff/', include('staff.urls')),
    path('students/', include('students.urls')),
    path('library/', include('library.urls')),
]
