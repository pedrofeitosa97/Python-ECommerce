# Generated by Django 4.1.7 on 2023-03-15 21:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="products",
            old_name="picture",
            new_name="picture_url",
        ),
    ]