# Generated by Django 3.0 on 2019-12-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['sir_name', 'first_name'], 'verbose_name_plural': 'staff'},
        ),
        migrations.AlterModelOptions(
            name='teachingstaff',
            options={'ordering': ['tsc_number'], 'verbose_name_plural': 'Teaching Staff'},
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='is_teacher_staff',
            new_name='is_teaching_staff',
        ),
        migrations.AddField(
            model_name='staff',
            name='emergency_contact_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='emergency_contact_relationship',
            field=models.CharField(help_text='Eg: Close Uncle', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='emergency_phone',
            field=models.IntegerField(help_text='Enter Emergency phone number', null=True),
        ),
    ]