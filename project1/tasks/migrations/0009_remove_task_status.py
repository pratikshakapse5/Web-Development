# Generated by Django 2.2.5 on 2020-04-14 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
