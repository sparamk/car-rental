# Generated by Django 4.1.1 on 2022-12-05 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0004_book_car_car"),
    ]

    operations = [
        migrations.AddField(
            model_name="book_car",
            name="subscription",
            field=models.CharField(default="silver", max_length=6),
        ),
    ]
