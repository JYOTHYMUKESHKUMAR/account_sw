# Generated by Django 5.0 on 2024-03-04 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0004_remove_dashboard_total_actual_cash_in_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summary',
            old_name='planned_balance',
            new_name='balance',
        ),
    ]
