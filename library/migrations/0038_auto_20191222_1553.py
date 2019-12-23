# Generated by Django 3.0.1 on 2019-12-22 15:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0037_auto_20191221_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=uuid.UUID('2b9aa8b8-8a0b-48b0-bc65-25e17c0beffc'), help_text='Unique ID for this particular book across whole library', max_length=20, primary_key=True, serialize=False),
        ),
    ]
