# Generated by Django 4.2.1 on 2023-05-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_pages_definition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='title_description',
            field=models.TextField(blank=True, default='Contact for details|', help_text='use | for next line', max_length=255, null=True),
        ),
    ]
