# Generated by Django 4.1 on 2023-09-21 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='cuatomer_name',
            new_name='customer_name',
        ),
    ]
