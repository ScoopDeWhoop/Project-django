# Generated by Django 4.2.3 on 2023-08-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_remove_book_id_remove_book_type_book_loan_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="image",
            field=models.ImageField(
                default="book_images/book_placeholder.jpg", upload_to="book_images"
            ),
        ),
    ]
