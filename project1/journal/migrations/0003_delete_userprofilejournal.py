# Generated by Django 2.2.5 on 2020-04-12 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_userprofilejournal'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileJournal',
        ),
    ]
