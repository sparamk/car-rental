# Generated by Django 4.1.1 on 2022-12-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0010_rename_user_id_book_car_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="book_car",
            name="session_id",
            field=models.TextField(default=""),
        ),
    ]