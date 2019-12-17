from django.db import models
from django.urls import reverse


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True, help_text="Enter Student ID")
    first_name = models.CharField(max_length=20, help_text="Enter First Name")
    sir_name = models.CharField(max_length=20, help_text="Enter Sir Name")
    other_name = models.CharField(max_length=20, help_text="Enter Other Name")
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('m', 'male'),
        ('f', 'female')
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    kcpe_marks = models.IntegerField(null=True, blank=True)
    primary_school = models.CharField(max_length=20, null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    is_enrolled = models.BooleanField(default=True)
    home_county = models.CharField(max_length=20, null=True, blank=True, help_text="Enter home County")
    home_town = models.CharField(max_length=20, null=True, blank=True, help_text="Enter home Town")
    health = models.TextField(max_length=500, null=True, blank=True, default="Good", help_text="Enter health status "
                                                                                               "or complications")
    emergency_contact_name = models.CharField(max_length=40)                                                                                           
    emergency_phone = models.IntegerField(help_text="Enter Emergency phone number")
    emergency_email = models.CharField(max_length=20, help_text="Enter email")
    father_alive = models.BooleanField(default=True, blank=True, help_text="Is the father alive?")
    mother_alive = models.BooleanField(default=True, blank=True, help_text="Is the mother alive?")

    def __str__(self):
        return f'{self.student_id}: {self.sir_name} {self.first_name}'

    class Meta:
        ordering = ['sir_name', 'first_name']

    def get_absolute_url(self):
        reverse('student_detail', args=[str(self.student_id)])
