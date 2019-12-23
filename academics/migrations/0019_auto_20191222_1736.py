# Generated by Django 3.0.1 on 2019-12-22 17:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0018_auto_20191221_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examperformance',
            old_name='stud',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='examperformance',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='examperformance',
            name='marks',
        ),
        migrations.RemoveField(
            model_name='examperformance',
            name='subject',
        ),
        migrations.AddField(
            model_name='examperformance',
            name='biology',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='examperformance',
            name='business',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='examperformance',
            name='chemistry',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='examperformance',
            name='computer',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='examperformance',
            name='english',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='examperformance',
            name='geography',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='examperformance',
            name='history',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='examperformance',
            name='kiswahili',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='examperformance',
            name='mathematics',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='examperformance',
            name='physics',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
