import django_filters

from academics.models import ExamPerformance, Exam, Subject, Classes, Stream
from students.models import Student


class ExamPerformanceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    subject = django_filters.ModelChoiceFilter(queryset=Subject.objects.all())
    grade = django_filters.ChoiceFilter(lookup_expr='iexact')
    student_id = django_filters.ModelMultipleChoiceFilter(queryset=Student.objects.all())
    stream = django_filters.ModelMultipleChoiceFilter(queryset=Stream.objects.all())
 #   stream = django_filters.CharFilter(queryset=Stream.objects.filter(student__Class__stream)

    # def get_stream(student):
    #     student = student
    #     student_query = Student.objects.filter(student_id=student)
    #     class_query = Classes.objects.filter(id=student_query)
    #     stream = Stream.objects.filter(id=class_query)
    #
    #     return stream
    #
    # stream = django_filters.ModelMultipleChoiceFilter(queryset=get_stream(student))

    marks = django_filters.RangeFilter()
