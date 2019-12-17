# Generated by Django 3.0 on 2019-12-17 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('national_id', models.IntegerField(help_text='Enter National ID. This is not editable!', primary_key=True, serialize=False)),
                ('is_teacher_staff', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=20)),
                ('sir_name', models.CharField(max_length=20)),
                ('other_name', models.CharField(blank=True, max_length=20, null=True)),
                ('kra_pin', models.CharField(max_length=11, unique=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('home_town', models.CharField(blank=True, max_length=20, null=True)),
                ('home_county', models.CharField(blank=True, max_length=20, null=True)),
                ('health_condition', models.TextField(blank=True, default='Good', help_text='Enter health status or complications', max_length=500, null=True)),
                ('is_employed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(help_text='Staff roles. Eg;Teacher,Cook,Secretary,e.t.c', max_length=20, unique=True)),
                ('role_function', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsc_number', models.IntegerField(unique=True)),
                ('staff_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.Staff')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='role',
            field=models.ForeignKey(help_text='Staff roles. Eg;Teacher,Cook,Secretary,e.t.c', null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.StaffRole'),
        ),
    ]
