from django.shortcuts import render
from django.http import HttpResponse

from students.models import Student, Father, Mother, Sponsor
from staff.models import Staff, TeachingStaff


def index(request):
    num_students = Student.objects.all().count()
    num_staff = Staff.objects.all().count()
    # orphan_students = Student.objects.filter(father_alive != True).count()

    context = {
        'num_students': num_students,
        'num_staff': num_staff,
        # 'orphan_students' : orphan_students
    }

    return render(request, 'index.html', context)
