# Generated by Django 4.2.1 on 2023-05-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_pages_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='slug',
            field=models.SlugField(blank=True, help_text='if leave it will take from title ', null=True),
        ),
    ]
