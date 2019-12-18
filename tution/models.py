from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

from staff.models import TeachingStaff
from students.models import Student
from academics.models import Subject, ClassNumeral


class Exam(models.Model):
    name = models.CharField(max_length=50, help_text="Example: 2019 End Term 1 Exam")
    TERMS = [('o', 'one'), ('tw', 'two'), ('th', 'three')]
    term = models.CharField(choices=TERMS)
    year = models.IntegerField(validators=[MaxValueValidator(3500), MinValueValidator(2020)])
    exam_start_date = models.DateField()
    subjects = models.ManyToManyField(Subject, help_text="Select Subjects")
    classes_involved = models.ManyToManyField(ClassNumeral)


class ExamPerformance(models.Model):
    name = models.ForeignKey(Exam, on_delete=models.PROTECT)
    subject = models.ManyToManyField(Subject)
    student = models.ManyToManyField(Student)
    marks = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(00)])


class Club(models.Model):
    club_name = models.CharField(max_length=20, help_text="Enter Club, Society or Organisation Name")
    club_purpose = models.TextField(max_length=30, blank=True, null=True)
    more_information = models.TextField(max_length=100, blank=True, null=True)
    teacher_lead = models.ManyToManyField(TeachingStaff, help_text="Select Teacher In Charge")
    teacher_assistant_lead = models.ManyToManyField(TeachingStaff, help_text="Select Teacher In Charge")
    members = models.ManyToManyField(Student, help_text="Select Student Members")
