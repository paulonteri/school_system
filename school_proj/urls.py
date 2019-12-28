from django.contrib import admin
from . admin import school_admin_site
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('school/', include('school.urls')),
    path('sysadmin/', admin.site.urls),
    path('admin/', school_admin_site.urls),
    path('staff/', include('staff.urls')),
    path('students/', include('students.urls')),
    path('library/', include('library.urls')),
    path('academics/', include('academics.urls')),
]
