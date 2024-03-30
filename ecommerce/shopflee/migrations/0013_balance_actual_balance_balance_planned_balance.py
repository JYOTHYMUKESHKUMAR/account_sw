# Generated by Django 5.0 on 2023-12-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopflee', '0012_rename_balance_amount_balance_balance_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='actual_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='balance',
            name='planned_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
