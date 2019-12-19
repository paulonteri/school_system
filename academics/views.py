from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from . models import Club, ExamPerformance, Exam, ClassNumeral, Classes, Subject


def index(request):
    return HttpResponse("<h1>Academics</h1>")