# Generated by Django 3.2 on 2021-12-14 00:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remembers', '0004_auto_20211214_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remember',
            name='showing_date',
            field=models.DateField(default=datetime.datetime(2021, 12, 21, 0, 58, 39, 89539), verbose_name='Showing Date'),
        ),
        migrations.AlterField(
            model_name='remember',
            name='stage',
            field=models.CharField(choices=[('1W', (('1 Week', '7'),)), ('2W', (('2 Week', '14'),)), ('1M', (('1 Month', '30'),)), ('2M', (('2 Month', '60'),)), ('3M', (('3 Month', '90'),)), ('6M', (('6 Month', '180'),)), ('1Y', (('1 Year', '360'),))], default='1W', max_length=10),
        ),
    ]
