# Generated by Django 4.1.2 on 2022-11-25 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesTaches', '0003_alter_task_due_date_alter_task_schedule_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 2, 13, 58, 48, 638345)),
        ),
    ]
