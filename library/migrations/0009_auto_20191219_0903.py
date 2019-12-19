# Generated by Django 3.0.1 on 2019-12-19 09:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_auto_20191218_1632'),
        ('library', '0008_auto_20191219_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=uuid.UUID('34c28c57-e9e5-421c-9af0-e8fb1e21218f'), help_text='Unique ID for this particular book across whole library', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='book',
            name='subject',
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.ForeignKey(help_text='Select Subject', null=True, on_delete=django.db.models.deletion.PROTECT, to='academics.Subject'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='type',
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(help_text='Select a book type', null=True, on_delete=django.db.models.deletion.PROTECT, to='library.BookType'),
        ),
    ]