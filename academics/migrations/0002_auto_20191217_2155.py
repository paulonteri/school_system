# Generated by Django 3.0 on 2019-12-17 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20191217_2045'),
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
    ]