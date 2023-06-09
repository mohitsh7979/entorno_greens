# Generated by Django 4.1.3 on 2023-03-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='media/profile_pic')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('o', 'other')], max_length=100)),
                ('designation', models.CharField(choices=[('s', 'Sales Officer'), ('t', 'Territory Exceutive'), ('f', 'Field Assistant'), ('g', 'General Manager'), ('h', 'HR Manager'), ('o', 'Office Management Staff'), ('c', 'CA'), ('d', 'Director'), ('D', 'Desk Office Assitant')], max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('pan_card', models.ImageField(upload_to='media/pan_card')),
                ('adhar_card', models.ImageField(upload_to='media/adhar_card')),
                ('cheque', models.ImageField(upload_to='media/bank_details')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
