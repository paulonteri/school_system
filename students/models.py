from django.db import models
from django.urls import reverse


class Student(models.Model):
    student_id = models.IntegerField(max_length=20, primary_key=True, help_text="Enter Student ID")
    first_name = models.CharField(max_length=20, help_text="Enter First Name")
    sir_name = models.CharField(max_length=20, help_text="Enter Sir Name")
    other_name = models.CharField(max_length=20, help_text="Enter Other Name")
    date_of_birth = models.DateField()
    KCPE_marks = models.IntegerField(max_length=3, null=True, blank=True)
    Primary_School = models.CharField(max_length=20, null=True, blank=True)
    Admission_Date = models.DateField(null=True, blank=True)
    Enrolled = models.BooleanField(default=True)
    Home_County = models.CharField(max_length=20, null=True, blank=True, help_text="Enter home County")
    Home_Town = models.CharField(max_length=20, null=True, blank=True, help_text="Enter home Town")
    Health_Complications = models.TextField(max_length=500, null=True, blank=True)
    emergency_phone = models.IntegerField(max_length=13, help_text="Enter Emergency phone number")
    emergency_email = models.CharFieldField(max_length=20, help_text="Enter email")
    father_alive = models.BooleanField(default=True, blank=True, help_text="Is the father alive?")
    mother_alive = models.BooleanField(default=True, blank=True, help_text="Is the mother alive?")

    def __str__(self):
        return f'{self.student_id},{self.sir_name},{self.first_name}'

    class Meta:
        ordering = ['sir_name', 'first_name']

    def get_absolute_url(self):
        reverse('student_detail', args=[str(self.student_id)])
