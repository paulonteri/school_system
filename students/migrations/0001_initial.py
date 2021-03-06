# Generated by Django 3.0.1 on 2019-12-18 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DormitoryName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Father',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Enter the first name of the student's male guardian", max_length=20)),
                ('sir_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mother',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Enter the first name of the student's female guardian", max_length=20)),
                ('sir_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, help_text='First name of sponsor if applicable', max_length=20, null=True)),
                ('sir_name', models.CharField(blank=True, help_text='Sir name of sponsor if applicable', max_length=20, null=True)),
                ('company_name', models.CharField(blank=True, help_text='Only if the Sponsor is a company', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(help_text='Enter Student ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='Enter First Name', max_length=20)),
                ('sir_name', models.CharField(help_text='Enter Sir Name', max_length=20)),
                ('other_name', models.CharField(help_text='Enter Other Name', max_length=20)),
                ('father_alive', models.BooleanField(blank=True, default=True, help_text='Is the father alive?')),
                ('mother_alive', models.BooleanField(blank=True, default=True, help_text='Is the mother alive?')),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=6)),
                ('kcpe_marks', models.IntegerField(blank=True, null=True)),
                ('primary_school', models.CharField(blank=True, max_length=20, null=True)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('is_enrolled', models.BooleanField(default=True, help_text='Is the student enrolled?')),
                ('home_county', models.CharField(blank=True, help_text='Enter home County', max_length=20, null=True)),
                ('home_town', models.CharField(blank=True, help_text='Enter home Town', max_length=20, null=True)),
                ('religion', models.CharField(blank=True, max_length=10, null=True)),
                ('health', models.TextField(blank=True, default='Good', help_text='Enter health status or complications', max_length=500, null=True)),
                ('emergency_contact_name', models.CharField(max_length=40)),
                ('emergency_contact_relationship', models.CharField(help_text='Eg: Close Uncle', max_length=10, null=True)),
                ('emergency_phone', models.IntegerField(help_text='Enter Emergency phone number')),
                ('premium', models.BooleanField(blank=True, default=False, help_text='Do not edit this')),
                ('Class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='academics.Classes')),
                ('dormitory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Dormitories')),
                ('female_guardian', models.ForeignKey(help_text="Select or Enter the details of the student's male guardian", null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Mother')),
                ('male_guardian', models.ForeignKey(help_text="Select or Enter the details of the student's male guardian", null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Father')),
                ('sponsor', models.ForeignKey(blank=True, help_text="(IF APPLICABLE ONLY) Select or Enter the details of the student's male guardian", null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Sponsor')),
            ],
            options={
                'ordering': ['sir_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='HealthIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=20)),
                ('issue', models.TextField(max_length=150)),
                ('treatment', models.TextField(blank=True, max_length=150, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaryIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=20)),
                ('issue', models.TextField(max_length=300)),
                ('outcome', models.TextField(blank=True, max_length=150, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]
