# Generated by Django 4.0 on 2021-12-31 06:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_create_date_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 31, 6, 25, 41, 978328, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 31, 6, 25, 41, 977477, tzinfo=utc)),
        ),
    ]
