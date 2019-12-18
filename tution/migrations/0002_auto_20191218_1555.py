# Generated by Django 3.0.1 on 2019-12-18 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ['name', 'purpose']},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['year', 'name']},
        ),
        migrations.RenameField(
            model_name='club',
            old_name='club_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='club_purpose',
            new_name='purpose',
        ),
    ]