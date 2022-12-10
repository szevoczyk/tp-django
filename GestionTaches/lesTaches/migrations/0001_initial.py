# Generated by Django 4.1.2 on 2022-11-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('schedule_date', models.DateField()),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
    ]
