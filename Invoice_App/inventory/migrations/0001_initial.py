# Generated by Django 4.1 on 2023-09-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
