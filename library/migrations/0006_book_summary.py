# Generated by Django 4.2.3 on 2023-08-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0005_remove_customer_age_remove_customer_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="summary",
            field=models.TextField(null=True),
        ),
    ]
