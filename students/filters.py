import django_filters

from students.models import Student, Sponsor, Father, Mother, Dormitories, DisciplinaryIssue, HealthIssue, Classes, \
    ClassNumeral, Stream
from academics.models import Stream


class StudentsFilter(django_filters.FilterSet):
    Class = django_filters.ModelChoiceFilter(queryset=Classes.objects.all())
    student_id = django_filters.NumberFilter(lookup_expr='icontains')
    sir_name = django_filters.CharFilter(lookup_expr='icontains')