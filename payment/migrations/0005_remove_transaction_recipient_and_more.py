# Generated by Django 4.2.4 on 2024-10-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_rename_receiving_wallet_transaction_recipient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='recipient',
        ),
        migrations.AddField(
            model_name='transaction',
            name='recipient_account_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='recipient_bank',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='recipient_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
