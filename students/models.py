from django.db import models
from django.urls import reverse

from academics.models import Classes, Stream, ClassNumeral


class Dormitories(models.Model):
    DormitoryName = models.CharField(max_length=20)


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True, help_text="Enter Student ID")
    class_ns = models.ForeignKey(Classes, null=True, on_delete=models.PROTECT)
    dormitory = models.ForeignKey(Dormitories, null=True, on_delete=models.PROTECT, blank=True)
    first_name = models.CharField(max_length=20, help_text="Enter First Name")
    sir_name = models.CharField(max_length=20, help_text="Enter Sir Name")
    other_name = models.CharField(max_length=20, help_text="Enter Other Name")
    father_alive = models.BooleanField(default=True, null=True,
                                       help_text="Is the father alive?")
    mother_alive = models.BooleanField(default=True, null=True, help_text="Is the mother alive?")
    father_first_name = models.CharField(max_length=20, null=True, help_text="Enter the first name of the student's "
                                                                             "male guardian")
    father_sir_name = models.CharField(max_length=20, null=True)
    father_email = models.EmailField(null=True)
    father_phone = models.IntegerField(null=True)
    father_premium = models.BooleanField(default=False, blank=True, help_text="Do not edit this")
    mother_first_name = models.CharField(max_length=20, null=True, help_text="Enter the first name of the student's "
                                                                             "female guardian")
    mother_sir_name = models.CharField(max_length=20, null=True)
    mother_email = models.EmailField(null=True)
    mother_phone = models.IntegerField(null=True)
    mother_premium = models.BooleanField(default=False, blank=True, help_text="Do not edit this")
    sponsor_first_name = models.CharField(blank=True, null=True, max_length=20,
                                          help_text="First name of sponsor if applicable")
    sponsor_sir_name = models.CharField(blank=True, null=True, max_length=20,
                                        help_text="Sir name of sponsor if applicable")
    sponsor_company_name = models.CharField(blank=True, null=True, max_length=20,
                                            help_text="Only if the Sponsor is a company")
    sponsor_premium = models.BooleanField(default=False, blank=True, help_text="Do not edit this")

    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('m', 'male'),
        ('f', 'female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    kcpe_marks = models.IntegerField(null=True, blank=True)
    primary_school = models.CharField(max_length=20, null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    is_enrolled = models.BooleanField(default=True, help_text="Is the student enrolled?")
    home_county = models.CharField(max_length=20, null=True, blank=True, help_text="Enter home County")
    home_town = models.CharField(max_length=20, null=True, blank=True, help_text="Enter home Town")
    religion = models.CharField(max_length=10, null=True, blank=True, )
    health = models.TextField(max_length=500, null=True, blank=True, default="Good", help_text="Enter health status "
                                                                                               "or complications")

    def __str__(self):
        return f'{self.student_id}: {self.sir_name} {self.first_name}'

    class Meta:
        ordering = ['sir_name', 'first_name']

    def get_absolute_url(self):
        reverse('student_detail', args=[str(self.student_id)])

    def display_Class(self):                # Class from students model
        return ','.join(i.Class.stream for i in self.Class.all()[:3])


class DisciplinaryIssue(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    issue = models.TextField(max_length=300)
    outcome = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.title}: {self.student}'

    class Meta:
        ordering = ['date', 'student']

    def get_absolute_url(self):
        reverse('Discipline', args=[str(self.title)])


class HealthIssue(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    issue = models.TextField(max_length=150)
    treatment = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.title}: {self.student}'

    class Meta:
        ordering = ['date', 'student']

    def get_absolute_url(self):
        reverse('Health', args=[str(self.title)])

