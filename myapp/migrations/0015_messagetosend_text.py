# Generated by Django 4.1 on 2022-08-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_messagetosend_sent_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetosend',
            name='text',
            field=models.TextField(default='testing'),
            preserve_default=False,
        ),
    ]
