from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

from staff.models import TeachingStaff
# from students.models import Student


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=15)
    hod = models.ForeignKey(TeachingStaff, on_delete=models.PROTECT, related_name="subjectHODs")


class ClassNumeral(models.Model):
    name = models.IntegerField(primary_key=True, help_text="For Example: 1,2,3. Streams (eg; east) will be added later",
                               validators=[MaxValueValidator(4), MinValueValidator(1)])

    class Meta:
        verbose_name_plural = "Class Numerals"


class Stream(models.Model):
    name = models.CharField(primary_key=True, max_length=15, help_text="For Example: East, Yellow, e.t.c")


class Classes(models.Model):
    Class = models.ForeignKey(ClassNumeral, on_delete=models.PROTECT)
    stream = models.ForeignKey(Stream, on_delete=models.PROTECT)
    class_teacher = models.ForeignKey(TeachingStaff, on_delete=models.PROTECT, related_name="classTeachers")
    assistant_class_teacher = models.ForeignKey(TeachingStaff, blank=True, null=True,
                                                on_delete=models.PROTECT,
                                                related_name="classes_assistantClassTeachers")
    year_of_graduation = models.IntegerField('Year of Graduation ', null=True, validators=[MaxValueValidator(3500), MinValueValidator(2020)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.Class, self.stream, self.year_of_grad}'

    class Meta:
        ordering = ['Class', 'stream']
        verbose_name_plural = "Classes"

    def get_absolute_url(self):
        reverse('classes', args=[str(self.id)])


class SubjectTeacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(TeachingStaff, on_delete=models.CASCADE)
    actively_teaching = models.BooleanField(default=True)

    class Meta:
        ordering = ['subject', 'teacher']
