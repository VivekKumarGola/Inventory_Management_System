# Generated by Django 4.1 on 2023-09-27 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_invoice_price_invoice_product_name_invoice_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('total', models.CharField(max_length=50)),
                ('invoide', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice', to='invoice.invoice')),
            ],
        ),
    ]