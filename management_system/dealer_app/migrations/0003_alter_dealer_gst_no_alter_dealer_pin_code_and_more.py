# Generated by Django 4.1.3 on 2023-03-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer_app', '0002_distributer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='Gst_No',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='Pin_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='Seed_License',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='Whatsapp_No',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='distributer',
            name='Gst_No',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='distributer',
            name='Pin_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='distributer',
            name='Seed_License',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='distributer',
            name='Whatsapp_No',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
