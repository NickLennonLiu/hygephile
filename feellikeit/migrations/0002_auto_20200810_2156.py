# Generated by Django 3.0.3 on 2020-08-10 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feellikeit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feellikeit',
            name='no',
            field=models.TextField(default="Just simply don't do that."),
        ),
        migrations.AddField(
            model_name='feellikeit',
            name='snap',
            field=models.ImageField(default='pics/never_mind.png', upload_to='snap'),
        ),
        migrations.AlterField(
            model_name='feellikeit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 21, 56, 11, 590503)),
        ),
    ]