# Generated by Django 5.0.2 on 2024-06-04 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing_info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billinginfo',
            old_name='adress',
            new_name='address',
        ),
    ]
