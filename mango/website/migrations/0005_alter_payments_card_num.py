# Generated by Django 5.1.6 on 2025-03-06 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_payments_card_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='card_num',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.MinLengthValidator(16)]),
        ),
    ]
