# Generated by Django 4.2.3 on 2023-08-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0003_book_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(default="email@email.com", max_length=254),
        ),
    ]
