# Generated by Django 5.1.1 on 2024-10-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='account_number',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='wallet_pin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
