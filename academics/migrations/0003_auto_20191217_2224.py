# Generated by Django 3.0 on 2019-12-17 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20191217_2045'),
        ('academics', '0002_auto_20191217_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassNumeral',
            fields=[
                ('name', models.IntegerField(help_text='For Example: 1,2,3. Streams (eg; east) will be added later', primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Class Numerals',
            },
        ),
        migrations.AlterModelOptions(
            name='classes',
            options={'ordering': ['Class', 'stream'], 'verbose_name_plural': 'Classes'},
        ),
        migrations.RenameField(
            model_name='classes',
            old_name='Stream',
            new_name='stream',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teachers',
        ),
        migrations.AlterField(
            model_name='stream',
            name='name',
            field=models.CharField(help_text='For Example: East, Yellow, e.t.c', max_length=15, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='SubjectTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actively_teaching', models.BooleanField(default=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.TeachingStaff')),
            ],
            options={
                'ordering': ['subject', 'teacher'],
            },
        ),
        migrations.AlterField(
            model_name='classes',
            name='Class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.ClassNumeral'),
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
