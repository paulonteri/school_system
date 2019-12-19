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
    Class = models.ForeignKey(ClassNumeral, on_delete=models.PROTECT)
    stream = models.ForeignKey(Stream, on_delete=models.PROTECT)
    class_teacher = models.ForeignKey(TeachingStaff, on_delete=models.PROTECT, related_name="classTeachers")
    assistant_class_teacher = models.ForeignKey(TeachingStaff, blank=True, null=True,
                                                on_delete=models.PROTECT,
                                                related_name="classes_assistantClassTeachers")
    year_of_graduation = models.IntegerField('Year of Graduation ', null=True,
                                             validators=[MaxValueValidator(3500), MinValueValidator(2020)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.Class.name, self.stream.name, self.year_of_graduation}'

    class Meta:
        ordering = ['Class', 'stream']
        verbose_name_plural = "Class + Streams (Normal Classes)"

    def get_absolute_url(self):
        reverse('classes', args=[str(self.id)])


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
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
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
