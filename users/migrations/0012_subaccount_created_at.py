# Generated by Django 4.2.4 on 2024-10-25 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_subaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='subaccount',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
