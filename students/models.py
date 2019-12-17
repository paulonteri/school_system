from django.db import models
from django.urls import reverse

from academics.models import Classes


class Father(models.Model):
    first_name = models.CharField(max_length=20, help_text="Enter the first name of the student's male guardian")
    sir_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.sir_name} {self.first_name}'


class Mother(models.Model):
    first_name = models.CharField(max_length=20, help_text="Enter the first name of the student's female guardian")
    sir_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.sir_name} {self.first_name}'


class Sponsor(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=20, help_text="First name of sponsor if applicable")
    sir_name = models.CharField(blank=True, null=True, max_length=20, help_text="Sir name of sponsor if applicable")
    company_name = models.CharField(blank=True, null=True, max_length=20, help_text="Only if the Sponsor is a company")

    def __str__(self):
        return f'{self.company_name} {self.sir_name} {self.first_name}'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True, help_text="Enter Student ID")
    Class = models.ForeignKey(Classes, null=True, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=20, help_text="Enter First Name")
    sir_name = models.CharField(max_length=20, help_text="Enter Sir Name")
    other_name = models.CharField(max_length=20, help_text="Enter Other Name")
    father_alive = models.BooleanField(default=True, blank=True,
                                       help_text="Is the father alive?")
    mother_alive = models.BooleanField(default=True, blank=True, help_text="Is the mother alive?")
    male_guardian = models.ForeignKey(Father, null=True,
                                      help_text="Select or Enter the details of the student's male guardian",
                                      on_delete=models.PROTECT)
    female_guardian = models.ForeignKey(Mother, null=True,
                                        help_text="Select or Enter the details of the student's male guardian",
                                        on_delete=models.PROTECT)
    sponsor = models.ForeignKey(Sponsor, null=True, help_text="(IF APPLICABLE ONLY) Select or Enter the details of "
                                                              "the student's male guardian",
                                on_delete=models.PROTECT)

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

    emergency_contact_name = models.CharField(max_length=40)
    emergency_contact_relationship = models.CharField(null=True, max_length=10, help_text="Eg: Close Uncle")
    emergency_phone = models.IntegerField(help_text="Enter Emergency phone number")
    premium = models.BooleanField(default=False, blank=True, help_text="Do not edit this")

    def __str__(self):
        return f'{self.student_id}: {self.sir_name} {self.first_name}'

    class Meta:
        ordering = ['sir_name', 'first_name']

    def get_absolute_url(self):
        reverse('student_detail', args=[str(self.student_id)])

