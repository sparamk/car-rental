# Generated by Django 4.1.1 on 2022-12-06 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0002_book_confirmation"),
        ("customer", "0003_alter_refer_friend_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="digital_check_in",
            name="book",
            field=models.ForeignKey(
                default="", on_delete=django.db.models.deletion.CASCADE, to="car.book"
            ),
        ),
    ]