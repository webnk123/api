# Generated by Django 4.1 on 2022-08-20 18:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_client_operator_code_alter_client_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^7\\d{10}')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='tag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
