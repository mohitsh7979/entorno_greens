# Generated by Django 4.1.3 on 2023-04-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer_app', '0005_alter_dealer_authorized_distributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='created_employee',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='distributer',
            name='created_employee',
            field=models.CharField(default='mohit', max_length=100),
            preserve_default=False,
        ),
    ]
