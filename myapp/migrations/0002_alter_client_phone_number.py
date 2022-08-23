# Generated by Django 4.1 on 2022-08-20 17:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]