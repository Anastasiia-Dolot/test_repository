# Generated by Django 3.1.7 on 2021-03-28 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 15, 1, 23, 178873, tzinfo=utc), verbose_name='Дата добавления'),
        ),
    ]
