from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from . filters import BookFilter
from library.models import Book, BookType, BorrowBookInstance, Subject, Author


def index(request):
    return HttpResponse("<h1>library</h1>")


class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "book_list.html"
    paginate_by = 20


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book_detail'
    template_name = 'book_detail.html'


def book_search(request):
    book_list = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list)
    return render(request, 'book_list_search.html', {'filter': book_filter})
