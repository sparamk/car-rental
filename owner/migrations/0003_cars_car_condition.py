# Generated by Django 4.1.1 on 2022-12-04 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("owner", "0002_coupons_cars_date_added"),
    ]

    operations = [
        migrations.AddField(
            model_name="cars",
            name="car_condition",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
