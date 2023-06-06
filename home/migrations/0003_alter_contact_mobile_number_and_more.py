# Generated by Django 4.2.1 on 2023-05-31 04:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_contact_mobile_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="Mobile_number",
            field=models.PositiveBigIntegerField(
                validators=[django.core.validators.MaxValueValidator(9999999999)]
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="Whatsapp_number",
            field=models.PositiveBigIntegerField(
                validators=[django.core.validators.MaxValueValidator(9999999999)]
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="alternative_number",
            field=models.PositiveBigIntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MaxValueValidator(9999999999)],
            ),
        ),
    ]
