from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from .filters import StudentsFilter
from students.models import Student


def index(request):
    return HttpResponse("<h1>Students</h1>")


# def student_search(request):
#     student_list = Student.objects.all()
#     student_filter = StudentsFilter(request.GET, queryset=student_list)
#     return render(request, 'student_list_search.html', {'filter': student_filter})

def student_search(request):
    student_list = Student.objects.exclude(is_enrolled=False)
    student_filter = StudentsFilter(request.GET, queryset=student_list)
    return render(request, 'student_list_search.html', {'filter': student_filter})


class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name = 'student_detail'
    template_name = 'student_detail.html'
