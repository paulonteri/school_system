# Generated by Django 3.0.1 on 2019-12-28 06:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0057_auto_20191228_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=uuid.UUID('cfbfed82-a08d-48cf-89f7-cbb0e2e066e6'), help_text='Unique ID for this particular book across whole library', max_length=20, primary_key=True, serialize=False),
        ),
    ]
