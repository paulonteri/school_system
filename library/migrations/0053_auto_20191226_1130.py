# Generated by Django 3.0.1 on 2019-12-26 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0052_auto_20191226_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=uuid.UUID('f919999e-3772-4053-8abd-97d47c20544d'), help_text='Unique ID for this particular book across whole library', max_length=20, primary_key=True, serialize=False),
        ),
    ]
