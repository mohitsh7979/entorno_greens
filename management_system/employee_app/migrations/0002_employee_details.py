# Generated by Django 4.1.3 on 2023-03-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_pic', models.ImageField(upload_to='media')),
                ('pan_card', models.ImageField(upload_to='media')),
            ],
        ),
    ]
