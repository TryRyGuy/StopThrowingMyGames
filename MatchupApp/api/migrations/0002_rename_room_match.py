# Generated by Django 5.0.1 on 2024-01-19 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Match',
        ),
    ]
