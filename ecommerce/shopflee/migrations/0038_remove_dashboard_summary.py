# Generated by Django 5.0 on 2024-01-06 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopflee', '0037_dashboard_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='summary',
        ),
    ]
