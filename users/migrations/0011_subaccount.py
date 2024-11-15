# Generated by Django 4.2.4 on 2024-10-24 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_wallet_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_reference', models.CharField(max_length=20)),
                ('barter_id', models.CharField(max_length=15)),
                ('virtual_account_number', models.CharField(max_length=10)),
                ('virtual_bank_name', models.CharField(max_length=100)),
                ('wallet', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_account', to='users.wallet')),
            ],
        ),
    ]
