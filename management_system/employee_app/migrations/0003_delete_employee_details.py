# Generated by Django 4.1.3 on 2023-03-27 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_employee_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='employee_details',
        ),
    ]
