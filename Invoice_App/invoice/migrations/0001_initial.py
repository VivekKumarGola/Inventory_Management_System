# Generated by Django 4.1 on 2023-09-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuatomer_name', models.CharField(max_length=50)),
                ('customer_gst', models.CharField(max_length=50)),
                ('phone', models.TextField(max_length=15)),
            ],
        ),
    ]
