# Generated by Django 4.1 on 2022-08-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_mailinglist_datetime_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='datetime_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='datetime_start',
            field=models.DateTimeField(),
        ),
    ]
