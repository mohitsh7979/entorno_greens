# Generated by Django 4.1.3 on 2023-02-24 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_Name', models.CharField(max_length=50)),
                ('Mobile_No', models.IntegerField(blank=True, null=True)),
                ('Whatsapp_No', models.IntegerField()),
                ('Address', models.CharField(max_length=30)),
                ('District', models.CharField(max_length=30)),
                ('Pin_code', models.IntegerField()),
                ('Gst_No', models.CharField(max_length=30)),
                ('Seed_License', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer_app.dealer')),
            ],
        ),
    ]
