# Generated by Django 4.2.3 on 2023-07-13 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo',
            name='estilo',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
