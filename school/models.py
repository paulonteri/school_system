from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from academics.models import ClassNumeral
from students.models import Student


class SchoolInfo(models.Model):
    school_name = models.CharField(max_length=50)
    school_motto = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.school_name}'


class FeePayable(models.Model):
    class_numeral = models.ForeignKey(ClassNumeral, on_delete=models.PROTECT)
    total_fee = models.IntegerField(validators=[MaxValueValidator(2000000), MinValueValidator(10000)])

    def __str__(self):
        return f'{self.class_numeral.name},{self.total_fee}'


class FeePaymentStatus(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_payable = models.ForeignKey(FeePayable, on_delete=models.PROTECT)
    fee_paid = models.IntegerField(validators=[MaxValueValidator(2000000), MinValueValidator(10000)])

    def __str__(self):
        return f'{self.student.name} Balance = {self.fee_paid.total_fee - self.fee_paid} out of {self.fee_payable.total_fee}'
