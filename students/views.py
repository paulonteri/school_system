from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from .filters import StudentsFilter
from students.models import Student
from .forms import StudentForm


def add_student_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "add_student.html", context)


def index(request):
    return HttpResponse("<h1>Students</h1>")


# def student_search(request):
#     student_list = Student.objects.all()
#     student_filter = StudentsFilter(request.GET, queryset=student_list)
#     return render(request, 'student_list_search.html', {'filter': student_filter})

def student_search(request):
    students = Student.objects.all()[0]
    # classes = students.male_guardian.objects.all()[0]
    # # for i in students:
    # #     return Class
    # f_name = Student.male_guardian.first_name.objects.all()
    # def index(request):
    #     num_students = Student.objects.all().count()
    #     num_staff = Staff.objects.all().count()
    #     students = Student.objects.all()
    #     teachers = TeachingStaff.objects.all()
    #     # orphan_students = Student.objects.filter(father_alive != True).count()
    #
    #     context = {
    #         'num_students': num_students,
    #         'num_staff': num_staff,
    #         'students': students,
    #         'teachers': teachers,
    student_list = Student.objects.exclude(is_enrolled=False)
    student_filter = StudentsFilter(request.GET, queryset=student_list)
    return render(request, 'student_list_search.html', {'filter': student_filter})


class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name = 'student_detail'
    template_name = 'student_detail.html'
