# Generated by Django 4.1 on 2023-10-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_rename_invoide_product_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='netamount',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='netamount',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
