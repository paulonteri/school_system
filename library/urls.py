from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='library_home'),
    path('books/', views.BookListView.as_view(), name="book_list"),
    path('books/<str:pk>', views.BookDetailView.as_view(), name="book_detail")
]