# Generated by Django 3.1.5 on 2023-05-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20230515_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='products_used',
            field=models.TextField(blank=True),
        ),
    ]
