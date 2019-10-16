# Generated by Django 2.0.6 on 2019-10-16 02:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wikiApp', '0003_auto_20191015_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedEntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Related_Title', models.CharField(max_length=100)),
                ('Related_Text', models.TextField(max_length=10000)),
                ('Related_Date', models.DateTimeField(default=datetime.datetime(2019, 10, 16, 2, 35, 48, 578868, tzinfo=utc))),
                ('Related_FileUpload', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('RelatedforeignKeyUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='newentrymodel',
            name='Entry_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 16, 2, 35, 48, 578244, tzinfo=utc)),
        ),
    ]