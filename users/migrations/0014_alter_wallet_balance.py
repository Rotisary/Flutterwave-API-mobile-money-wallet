# Generated by Django 4.2.4 on 2024-11-12 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]