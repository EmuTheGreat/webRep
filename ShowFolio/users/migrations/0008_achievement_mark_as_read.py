# Generated by Django 4.2.2 on 2023-06-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_achievement"),
    ]

    operations = [
        migrations.AddField(
            model_name="achievement",
            name="mark_as_read",
            field=models.BooleanField(default=False),
        ),
    ]