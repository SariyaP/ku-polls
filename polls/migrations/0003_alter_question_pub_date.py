# Generated by Django 5.1 on 2024-09-03 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_end_date_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 3, 7, 52, 42, 197409, tzinfo=datetime.timezone.utc)),
        ),
    ]
