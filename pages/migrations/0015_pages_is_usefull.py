# Generated by Django 4.2.1 on 2023-06-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0014_pages_meta_description_pages_meta_keywords_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pages",
            name="is_usefull",
            field=models.BooleanField(default=False),
        ),
    ]
