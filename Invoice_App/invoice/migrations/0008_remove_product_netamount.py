# Generated by Django 4.1 on 2023-10-05 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_invoice_netamount_product_netamount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='netamount',
        ),
    ]
