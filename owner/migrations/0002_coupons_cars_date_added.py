# Generated by Django 4.1.1 on 2022-12-04 18:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("owner", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupons",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("coupon_code", models.CharField(max_length=20)),
                ("discount", models.CharField(max_length=2)),
                ("date_valid_from", models.DateField()),
                ("date_valid_to", models.DateField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name="cars",
            name="date_added",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]