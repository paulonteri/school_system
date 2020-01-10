from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'class_ns', 'dormitory', 'first_name', 'sir_name', 'other_name', 'father_alive',
                  'mother_alive', 'father_first_name', 'father_sir_name', 'father_email', 'father_phone',
                  'father_premium', 'mother_first_name', 'mother_email', 'mother_phone', 'mother_premium',
                  'sponsor_first_name', 'sponsor_sir_name', 'sponsor_company_name', 'sponsor_premium', 'date_of_birth',
                  'gender', 'kcpe_marks', 'primary_school', 'admission_date', 'is_enrolled', 'home_county', 'home_town',
                  'religion', 'health']
