# Generated by Django 3.0.1 on 2019-12-20 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20191220_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='emergency_contact_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='emergency_contact_relationship',
        ),
        migrations.RemoveField(
            model_name='student',
            name='emergency_phone',
        ),
    ]
