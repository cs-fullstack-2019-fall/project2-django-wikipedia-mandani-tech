# Generated by Django 2.0.6 on 2019-10-16 18:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wikiApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewEntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entry_Title', models.CharField(max_length=100)),
                ('Entry_Text', models.TextField(max_length=10000)),
                ('Entry_Date', models.DateTimeField(default=datetime.datetime(2019, 10, 16, 18, 24, 14, 564437, tzinfo=utc))),
                ('Entry_FileUpload', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('foreignKeyUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedEntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Related_Title', models.CharField(max_length=100)),
                ('Related_Text', models.TextField(max_length=10000)),
                ('Related_Date', models.DateTimeField(default=datetime.datetime(2019, 10, 16, 18, 24, 14, 565153, tzinfo=utc))),
                ('Related_FileUpload', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('RelatedforeignKeyUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wikiApp.NewEntryModel')),
            ],
        ),
    ]
