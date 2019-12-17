from django.db import models


class StaffRole(models.Model):
    role = models.CharField(max_length=20, unique=True, help_text="Staff roles. Eg;Teacher,Cook,Secretary,e.t.c")
    role_function = models.TextField(max_length=500)

    def __str__(self):
        return self.role


class Staff(models.Model):
    role = models.ForeignKey(StaffRole, on_delete=models.SET_NULL, help_text="Staff roles. Eg;Teacher,Cook,"
                                                                             "Secretary,e.t.c", null=True)
    first_name = models.CharField(max_length=20)
    sir_name = models.CharField(max_length=20)
    other_name = models.CharField(blank=True, null=True, max_length=20)
    national_id = models.IntegerField(primary_key=True, help_text="Enter National ID. This is not "
                                                                  "editable!")
    kra_pin = models.CharField(max_length=11, unique=True)
    phone = models.IntegerField()
    email = models.EmailField()
    home_town = models.CharField(max_length=20, null=True, blank=True)
    home_county = models.CharField(max_length=20, null=True, blank=True)
    health_condition = models.TextField(max_length=500, null=True, blank=True, default="Good", help_text="Enter "
                                                                                                         "health "
                                                                                                         "status or "
                                                                                                         "complications")
    is_employed = models.BooleanField(default=True)
    is_teacher_staff = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.sir_name};{self.first_name},({self.role.role})'


class TeachingStaff(models.Model):
    # subjects
    staff_info = models.OneToOneField(Staff, on_delete=models.CASCADE
                                      )
    tsc_number = models.IntegerField(unique=True)
