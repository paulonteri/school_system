from django.contrib import admin

from students.models import Student
from staff.models import Staff, StaffRole, TeachingStaff

# Register your models here.

# @admin.register(StaffRole)

admin.site.register(Staff)
admin.site.register(StaffRole)
admin.site.register(TeachingStaff)
admin.site.register(Student)

