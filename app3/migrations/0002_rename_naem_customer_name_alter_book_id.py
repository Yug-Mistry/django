# Generated by Django 4.2.6 on 2023-10-08 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app3", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="naem",
            new_name="name",
        ),
        migrations.AlterField(
            model_name="book",
            name="id",
            field=models.IntegerField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
    ]