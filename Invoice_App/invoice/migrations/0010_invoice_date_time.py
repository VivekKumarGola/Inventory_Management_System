# Generated by Django 4.1 on 2023-10-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_product_netamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='date_time',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]