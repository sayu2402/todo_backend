# Generated by Django 5.0.1 on 2024-02-19 07:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("basic", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="descriotion",
            new_name="description",
        ),
    ]