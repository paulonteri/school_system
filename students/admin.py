from django.contrib import admin

from students.models import Student, Father, Mother, Sponsor
from staff.models import Staff, StaffRole, TeachingStaff
from academics.models import Subject, ClassNumeral, Stream, Classes
from school.models import SchoolInfo, FeePayable, FeePaymentStatus

# Register your models here.

# @admin.register(StaffRole)

admin.site.register(Staff)
admin.site.register(StaffRole)
admin.site.register(TeachingStaff)
admin.site.register(Student)
admin.site.register(Father)
admin.site.register(Mother)
admin.site.register(Sponsor)
admin.site.register(Subject)
admin.site.register(ClassNumeral)
admin.site.register(Stream)
admin.site.register(Classes)
admin.site.register(SchoolInfo)
admin.site.register(FeePayable)
admin.site.register(FeePaymentStatus)


