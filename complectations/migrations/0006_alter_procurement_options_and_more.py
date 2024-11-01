# Generated by Django 5.1.2 on 2024-10-31 08:58

import complectations.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0005_procurement_procent_procurement_xlsx_file_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='procurement',
            options={'ordering': ['-id'], 'verbose_name': 'Закупка', 'verbose_name_plural': 'Закупки'},
        ),
        migrations.AlterField(
            model_name='procurement',
            name='payment_status',
            field=models.CharField(choices=[('Оплатил', 'Оплатил'), ('Не оплатил', 'Не оплатил')], default='Не оплатил', max_length=15, verbose_name='Статус оплаты'),
        ),
        migrations.AlterField(
            model_name='procurement',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Сумма чека'),
        ),
        migrations.AlterField(
            model_name='procurement',
            name='xlsx_file',
            field=models.FileField(blank=True, null=True, upload_to=complectations.utils.procurements_xlsx_upload_to, verbose_name='Excel файл сметы'),
        ),
    ]