# Generated by Django 4.1.7 on 2023-03-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_employees_hire_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='location',
        ),
        migrations.AddField(
            model_name='employees',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
