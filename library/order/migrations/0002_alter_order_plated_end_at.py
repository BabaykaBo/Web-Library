# Generated by Django 4.2 on 2023-04-27 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='plated_end_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 11, 11, 6, 1, 521197)),
        ),
    ]
