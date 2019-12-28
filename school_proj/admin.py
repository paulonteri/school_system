from django.contrib.admin import AdminSite


class EventAdminSite(AdminSite):
    site_header = "School Admin"
    site_title = "School Admin"
    index_title = "Welcome to The School Admin"
#   Paul was helped by Andre` to build this.


school_admin_site = EventAdminSite(name='school_admin')


from students.models import Student, DisciplinaryIssue, HealthIssue, Dormitories
from staff.models import Staff, StaffRole, TeachingStaff
from academics.models import Subject, ClassNumeral, Stream, Classes, SubjectTeacherClass, Exam, ExamPerformance, Club
from school.models import SchoolInfo, FeePayable, FeePaymentStatus
from library.models import Book, BookType, BorrowBookInstance, Author

# Register your models here.

# @admin.register(StaffRole)

school_admin_site.register(Staff)
school_admin_site.register(StaffRole)
school_admin_site.register(TeachingStaff)
school_admin_site.register(Student)
school_admin_site.register(Subject)
school_admin_site.register(ClassNumeral)
school_admin_site.register(Stream)
school_admin_site.register(Classes)
school_admin_site.register(SchoolInfo)
school_admin_site.register(FeePayable)
school_admin_site.register(FeePaymentStatus)
school_admin_site.register(Exam)
school_admin_site.register(ExamPerformance)
school_admin_site.register(Club)
school_admin_site.register(Author)
school_admin_site.register(BorrowBookInstance)
school_admin_site.register(Book)
school_admin_site.register(BookType)
school_admin_site.register(DisciplinaryIssue)
school_admin_site.register(HealthIssue)
school_admin_site.register(Dormitories)
school_admin_site.register(SubjectTeacherClass)
