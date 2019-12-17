from django.db import models

from academics.models import ClassNumeral
from students.models import Student


class SchoolInfo(models.Model):
    school_name = models.CharField(max_length=50)
    school_motto = models.CharField(max_length=50)


class FeePayable(models.Model):
    class_numeral = models.ForeignKey(ClassNumeral, on_delete=models.PROTECT)
    total_fee = models.IntegerField()


class FeePaymentStatus:
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_payable = models.ForeignKey(FeePayable, on_delete=models.PROTECT)
    fee_paid = models.IntegerField()
