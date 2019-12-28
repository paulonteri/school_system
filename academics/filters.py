import django_filters

from academics.models import ExamPerformance, Exam, Subject, Classes, Stream, ExamPerformanceView
from students.models import Student


class ExamPerformanceFilter(django_filters.FilterSet):
    exam_name = django_filters.CharFilter(lookup_expr='icontains')
    # subject = django_filters.ModelMultipleChoiceFilter(queryset=Subject.objects.all())
    # grade = django_filters.ChoiceFilter()
    student_id = django_filters.ModelMultipleChoiceFilter(queryset=Student.objects.all())
    stream = django_filters.ModelMultipleChoiceFilter(queryset=Stream.objects.all())
    english = django_filters.RangeFilter()
    kiswahili = django_filters.RangeFilter()
    mathematics = django_filters.RangeFilter()
    science = django_filters.RangeFilter()
    social_studies = django_filters.RangeFilter()
    religious_education = django_filters.RangeFilter()
    total = django_filters.RangeFilter()
