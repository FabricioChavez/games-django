# Generated by Django 5.0.2 on 2024-06-04 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_contains_offer', '0001_initial'),
        ('shopping_car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carcontainsoffer',
            name='shopping_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers_contained', to='shopping_car.shoppingcar'),
        ),
    ]
