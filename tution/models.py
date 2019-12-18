from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

from staff.models import TeachingStaff
from students.models import Student
from academics.models import Subject, ClassNumeral


class Exam(models.Model):
    name = models.CharField(max_length=50, help_text="Example: 2019 End Term 1 Exam")
    TERMS = [('o', 'one'), ('tw', 'two'), ('th', 'three')]
    term = models.CharField(choices=TERMS, max_length=4)
    year = models.IntegerField(validators=[MaxValueValidator(3500), MinValueValidator(2020)])
    exam_start_date = models.DateField()
    subjects = models.ManyToManyField(Subject, help_text="Select Subjects")
    classes_involved = models.ManyToManyField(ClassNumeral)

    def __str__(self):
        return f'{self.name}: {self.term} {self.year}'

    class Meta:
        ordering = ['year', 'name']

    def get_absolute_url(self):
        reverse('exam_detail', args=[str(self.name)])


class ExamPerformance(models.Model):
    name = models.ForeignKey(Exam, on_delete=models.PROTECT)
    subject = models.ManyToManyField(Subject)
    student = models.ManyToManyField(Student)
    marks = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(00)])

    def __str__(self):
        return f'{self.name}: {self.name.term} {self.name.year}'

    def get_absolute_url(self):
        reverse('exam_performance_detail', args=[str(self.name)])


class Club(models.Model):
    name = models.CharField(max_length=20, help_text="Enter Club, Society or Organisation Name")
    purpose = models.TextField(max_length=30, blank=True, null=True)
    more_information = models.TextField(max_length=100, blank=True, null=True)
    teacher_lead = models.ManyToManyField(TeachingStaff, help_text="Select Teacher In Charge",
                                          related_name="Teacher_Leads")
    teacher_assistant_lead = models.ManyToManyField(TeachingStaff, help_text="Select assistant Teacher",
                                                    related_name="Assistant_Teacher_Leads")
    members = models.ManyToManyField(Student, help_text="Select Student Members")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name', 'purpose']

    def get_absolute_url(self):
        reverse('club_detail', args=[str(self.name)])

    def get_club_members(self):
        return ','.join(members.first_name and members.student_id for members in self.membersall()[:100])
