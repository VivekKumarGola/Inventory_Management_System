# Generated by Django 4.1 on 2023-09-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_alter_invoice_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='product_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
