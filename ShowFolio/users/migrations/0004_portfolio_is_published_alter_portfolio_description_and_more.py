# Generated by Django 4.2.2 on 2023-06-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_portfolio_portfoliolike_portfoliofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
