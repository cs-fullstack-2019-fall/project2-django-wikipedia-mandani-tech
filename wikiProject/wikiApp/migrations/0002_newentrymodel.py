# Generated by Django 2.0.6 on 2019-10-15 17:56

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
                ('Entry_Date', models.DateTimeField(default=datetime.datetime(2019, 10, 15, 17, 56, 15, 772001, tzinfo=utc))),
                ('Entry_FileUpload', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('foreignKeyUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
