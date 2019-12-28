from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from academics.models import Club, ExamPerformance, Exam, ClassNumeral, Classes, Subject, ExamPerformanceView
from . filters import ExamPerformanceFilter


def index(request):
    return HttpResponse("<h1>Academics</h1>")


def exam_performance_search(request):
    exam_list = ExamPerformanceView.objects.all()
    exam_filter = ExamPerformanceFilter(request.GET, queryset=exam_list)
    return render(request, 'exam_performance_filter.html', {'filter': exam_filter})
