# Generated by Django 4.1 on 2023-10-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_remove_product_netamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='netamount',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]