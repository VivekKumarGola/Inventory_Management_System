# Generated by Django 4.1 on 2023-09-27 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='invoide',
            new_name='invoice',
        ),
    ]
