# Generated by Django 4.1.3 on 2023-01-28 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_registraion_registration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='course',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='gender',
        ),
    ]
