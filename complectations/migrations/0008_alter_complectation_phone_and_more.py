# Generated by Django 5.1.2 on 2024-11-01 10:07

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0007_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complectation',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон заказчика'),
        ),
        migrations.AlterField(
            model_name='service',
            name='payment_status',
            field=models.CharField(choices=[('Оплатил', 'Оплатил'), ('Не оплатил', 'Не оплатил')], default='Не оплатил', max_length=15, verbose_name='Статус оплаты'),
        ),
    ]
