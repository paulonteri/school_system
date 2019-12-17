# Generated by Django 3.0 on 2019-12-17 21:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0003_auto_20191217_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('name', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('name', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('hod', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subjectHODs', to='staff.TeachingStaff')),
                ('teachers', models.ManyToManyField(to='staff.TeachingStaff')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_graduation', models.DateField(validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(2020)])),
                ('active', models.BooleanField(default=False)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.Class')),
                ('Stream', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.Stream')),
                ('assistant_class_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='classes_assistantClassTeachers', to='staff.TeachingStaff')),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classTeachers', to='staff.TeachingStaff')),
            ],
        ),
    ]