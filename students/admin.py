from django.contrib import admin

from students.models import Student, Father, Mother, Sponsor, DisciplinaryIssue, HealthIssue, Dormitories
from staff.models import Staff, StaffRole, TeachingStaff
from academics.models import Subject, ClassNumeral, Stream, Classes
from school.models import SchoolInfo, FeePayable, FeePaymentStatus
from tution.models import Exam, ExamPerformance, Club
from library.models import Book, BookType, BorrowBookInstance, Author

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
admin.site.register(Exam)
admin.site.register(ExamPerformance)
admin.site.register(Club)
admin.site.register(Author)
admin.site.register(BorrowBookInstance)
admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(DisciplinaryIssue)
admin.site.register(HealthIssue)
admin.site.register(Dormitories)


