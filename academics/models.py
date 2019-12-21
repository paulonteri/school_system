from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

from staff.models import TeachingStaff


# from students.models import Student


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=15)
    hod = models.ForeignKey(TeachingStaff, on_delete=models.PROTECT, related_name="subjectHODs")

    class Meta:
        verbose_name_plural = "Subjects"

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        reverse('Subject', args=[str(self.name)])


class ClassNumeral(models.Model):
    name = models.IntegerField(primary_key=True, help_text="For Example: 1,2,3. Streams (eg; east) will be added later",
                               validators=[MaxValueValidator(4), MinValueValidator(1)])

    class Meta:
        verbose_name_plural = "Class Numerals"

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        reverse('Class_Numeral', args=[str(self.name)])


class Stream(models.Model):
    name = models.CharField(primary_key=True, max_length=15, help_text="For Example: East, Yellow, e.t.c")

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        reverse('Stream', args=[str(self.name)])


class Classes(models.Model):
    class_numeral = models.ForeignKey(ClassNumeral, on_delete=models.PROTECT)
    stream = models.ForeignKey(Stream, on_delete=models.PROTECT)
    class_teacher = models.ForeignKey(TeachingStaff, on_delete=models.PROTECT, related_name="classTeachers")
    assistant_class_teacher = models.ForeignKey(TeachingStaff, blank=True, null=True,
                                                on_delete=models.PROTECT,
                                                related_name="classes_assistantClassTeachers")
    year_of_graduation = models.IntegerField('Year of Graduation ', null=True,
                                             validators=[MaxValueValidator(3500), MinValueValidator(2020)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.class_numeral.name, self.stream.name, self.year_of_graduation}'

    class Meta:
        ordering = ['class_numeral', 'stream']
        verbose_name_plural = "Class + Streams (Normal Classes)"

    def get_absolute_url(self):
        reverse('classes', args=[str(self.id)])


class StudentClassStreamView(models.Model):
    student_id = models.IntegerField(primary_key=True, help_text="Enter Student ID")
    class_stream = models.ForeignKey(Classes, null=True, on_delete=models.PROTECT)
    dormitory = models.ForeignKey('students.Dormitories', null=True, on_delete=models.PROTECT, blank=True)
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
    health = models.TextField(max_length=500, null=True, blank=True, default="Good", help_text="Enter health status ")
    class_numeral = models.ForeignKey(ClassNumeral, on_delete=models.PROTECT)
    stream = models.ForeignKey(Stream, on_delete=models.PROTECT)
    class_teacher = models.ForeignKey(TeachingStaff, on_delete=models.PROTECT, related_name="classTeachersStaff")
    assistant_class_teacher = models.ForeignKey(TeachingStaff, blank=True, null=True,
                                                on_delete=models.PROTECT,
                                                related_name="classes_assistantClassTeachersStaffzz")
    year_of_graduation = models.IntegerField('Year of Graduation ', null=True,
                                             validators=[MaxValueValidator(3500), MinValueValidator(2020)])
    active = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = "student_class_stream_view"


# join table
class SubjectTeacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(TeachingStaff, on_delete=models.CASCADE)
    actively_teaching = models.BooleanField(default=True)

    class Meta:
        ordering = ['subject', 'teacher']

    def __str__(self):
        return f'{self.subject}: {self.teacher.staff_info.sir_name} {self.teacher.staff_info.first_name}'

    def get_absolute_url(self):
        reverse('Subject_Teacher', args=[str(self.id)])


from random import seed
from random import random

def return_random():
    return random()


class Exam(models.Model):
    name = models.CharField(max_length=50, help_text="Example: End Term ")
    TERMS = [('Term Two', 'Term One'), ('Term Two', 'Term Two'), (' Term Three', ' Term Three')]
    term = models.CharField(choices=TERMS, max_length=11)
    year = models.IntegerField(validators=[MaxValueValidator(3500), MinValueValidator(2020)])
    exam_start_date = models.DateField()
    subjects = models.ManyToManyField(Subject, help_text="Select Subjects")
    classes_involved = models.ManyToManyField(ClassNumeral)

    def __str__(self):
        return f'{self.name} ({self.term}: {self.year})'

    class Meta:
        ordering = ['year', 'name']

    def get_absolute_url(self):
        reverse('exam_detail', args=[str(self.name)])


class ExamPerformance(models.Model):
    name = models.ForeignKey(Exam, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    # function to get:
    # student.classes
    # student.classes.stream
    # student.classes.Class
    # get a method that automatically adds the grade
    # who recorded?
    stud = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    marks = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(00)])
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('A', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('Z', 'Z'),
    ]
    grade = models.CharField(null=True, choices=GRADE_CHOICES, max_length=1)

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
    members = models.ManyToManyField('students.Student', help_text="Select Student Members")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name', 'purpose']

    def get_absolute_url(self):
        reverse('club_detail', args=[str(self.name)])

    def get_club_members(self):
        return ','.join(members.first_name and members.student_id for members in self.members.all()[:100])


class SubjectTeacherClass(models.Model):
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    teacher = models.ForeignKey(SubjectTeacher, on_delete=models.PROTECT)

    class Meta:
        ordering = ['Class', 'teacher']

    def get_absolute_url(self):
        reverse('subject_teacher_class', args=[str(self.name)])

    def __str__(self):
        return f'{self.Class}: {self.teacher} {self.teacher.subject}'
