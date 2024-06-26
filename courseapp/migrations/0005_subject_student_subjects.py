# Generated by Django 5.0.4 on 2024-05-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0004_student_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(to='courseapp.subject'),
        ),
    ]
