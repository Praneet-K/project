# Generated by Django 3.1.2 on 2021-07-17 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
