# Generated by Django 4.1.1 on 2022-12-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("owner", "0008_cars_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="cars",
            name="cost_of_vehicle",
            field=models.CharField(default=2000, max_length=6),
        ),
        migrations.AddField(
            model_name="cars",
            name="rent_per_hour",
            field=models.CharField(default=1, max_length=6),
        ),
        migrations.AlterField(
            model_name="cars",
            name="car_condition",
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name="cars",
            name="subscription",
            field=models.CharField(default="silver", max_length=6),
        ),
    ]
