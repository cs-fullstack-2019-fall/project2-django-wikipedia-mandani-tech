# Generated by Django 2.0.6 on 2019-10-16 02:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0004_auto_20191016_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newentrymodel',
            name='Entry_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 16, 2, 36, 41, 665145, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='relatedentrymodel',
            name='Related_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 16, 2, 36, 41, 665775, tzinfo=utc)),
        ),
    ]