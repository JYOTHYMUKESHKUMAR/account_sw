# Generated by Django 5.0 on 2024-04-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0008_remove_dashboard_balance_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('project', models.CharField(max_length=250)),
                ('cash_in', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cash_out', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
