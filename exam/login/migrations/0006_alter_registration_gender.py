# Generated by Django 4.1.3 on 2023-01-31 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_registration_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('female', 'FEMALE'), ('male', 'MALE')], default=True, max_length=25),
        ),
    ]
