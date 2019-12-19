import django_filters
from library.models import Book, BookType, BorrowBookInstance, Subject, Author


# class ProductFilter(django_filters.FilterSet):
#     price = django_filters.NumberFilter()
#     price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
#     price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
#
#     release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
#     release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
#     release_year__lt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')
#
#     manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')
#
#     class Meta:
#         model = Product

##################################################################################################

# To prevent repetition

# class ProductFilter(django_filters.FilterSet):
#     class Meta:
#         model = Product
#         fields = {
#             'price': ['lt', 'gt'],
#             'release_date': ['exact', 'year__gt'],
#         }

# related models

# class ProductFilter(django_filters.FilterSet):
#     class Meta:
#         model = Product
#         fields = ['manufacturer__country']

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all())
    type = django_filters.ModelChoiceFilter(queryset=BookType.objects.all())
    subject = django_filters.ModelMultipleChoiceFilter(queryset=Subject.objects.all())

